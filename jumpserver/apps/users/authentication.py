# -*- coding: utf-8 -*-
#

import base64
import uuid
import hashlib
import time

from django.core.cache import cache
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.six import text_type
from django.utils.translation import ugettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework import authentication, exceptions, permissions
from rest_framework.authentication import CSRFCheck

from common.utils import get_object_or_none, make_signature, http_to_unixtime
from .utils import refresh_token
from .models import User, AccessKey, PrivateToken


def get_request_date_header(request):
    date = request.META.get('HTTP_DATE', b'')
    if isinstance(date, text_type):
        # Work around django test client oddness
        date = date.encode(HTTP_HEADER_ENCODING)
    return date


class AccessKeyAuthentication(authentication.BaseAuthentication):
    # coco luna 请求的时候用到
    # from rest_framework.authentication import CSRFCheck
    # 自定义认证继承 BaseAuthentication
    # authenticate 重写方法

    """App使用Access key进行签名认证, 目前签名算法比较简单,
    app注册或者手动建立后,会生成 access_key_id 和 access_key_secret,
    然后使用 如下算法生成签名:
    Signature = md5(access_key_secret + '\n' + Date)
    example: Signature = md5('d32d2b8b-9a10-4b8d-85bb-1a66976f6fdc' + '\n' +
                    'Thu, 12 Jan 2017 08:19:41 GMT')
    请求时设置请求header
    header['Authorization'] = 'Sign access_key_id:Signature' 如:
    header['Authorization'] =
        'Sign d32d2b8b-9a10-4b8d-85bb-1a66976f6fdc:OKOlmdxgYPZ9+SddnUUDbQ=='

    验证时根据相同算法进行验证, 取到access_key_id对应的access_key_id, 从request
    headers取到Date, 然后进行md5, 判断得到的结果是否相同, 如果是认证通过, 否则 认证
    失败
    """
    keyword = 'Sign'
    model = AccessKey

    def authenticate(self, request):

        auth = authentication.get_authorization_header(request).split() # 获取头 后分隔 后进行判断

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        # 得到的长度不等于2 都是不能通过，直接抛异常
        if len(auth) == 1:
            msg = _('Invalid signature header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid signature header. Signature '
                    'string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            sign = auth[1].decode().split(':')
            if len(sign) != 2:
                msg = _('Invalid signature header. '
                        'Format like AccessKeyId:Signature')
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = _('Invalid signature header. '
                    'Signature string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        access_key_id = sign[0]
        try:
            uuid.UUID(access_key_id)
        except ValueError:
            raise exceptions.AuthenticationFailed('Access key id invalid')
        request_signature = sign[1]

        return self.authenticate_credentials(
            request, access_key_id, request_signature)

    @staticmethod
    def authenticate_credentials(request, access_key_id, request_signature):
        access_key = get_object_or_none(AccessKey, id=access_key_id)
        request_date = get_request_date_header(request)
        # 通过数据监测后 验证时间 等等
        if access_key is None or not access_key.user:
            raise exceptions.AuthenticationFailed(_('Invalid signature.'))
        access_key_secret = access_key.secret

        try:
            request_unix_time = http_to_unixtime(request_date)
        except ValueError:
            raise exceptions.AuthenticationFailed(
                _('HTTP header: Date not provide '
                  'or not %a, %d %b %Y %H:%M:%S GMT'))

        if int(time.time()) - request_unix_time > 15 * 60:
            raise exceptions.AuthenticationFailed(
                _('Expired, more than 15 minutes'))

        signature = make_signature(access_key_secret, request_date)
        # 生成签名 比对 验证不通过抛异常
        if not signature == request_signature:
            raise exceptions.AuthenticationFailed(_('Invalid signature.'))

        if not access_key.user.is_active:
            raise exceptions.AuthenticationFailed(_('User disabled.'))
        return access_key.user, None


class AccessTokenAuthentication(authentication.BaseAuthentication):
    # authentication
    # 如果请求头中含有 Bearer adsffkey
    # 取到后进行验证
    keyword = 'Bearer'
    model = User
    expiration = settings.CONFIG.TOKEN_EXPIRATION or 3600

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Sign string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Sign string '
                    'should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(token)

    @staticmethod
    def authenticate_credentials(token):
        user_id = cache.get(token)
        user = get_object_or_none(User, id=user_id)

        if not user:
            msg = _('Invalid token or cache refreshed.')
            raise exceptions.AuthenticationFailed(msg)
        refresh_token(token, user)
        # 最终返回用户 或者None
        return user, None


class PrivateTokenAuthentication(authentication.TokenAuthentication):
    # 重写
    model = PrivateToken


class SessionAuthentication(authentication.SessionAuthentication):
    # session认证方式
    # 测试使用
    def enforce_csrf(self, request):
        reason = CSRFCheck().process_view(request, None, (), {})
        if reason:
            raise exceptions.AuthenticationFailed(reason)
