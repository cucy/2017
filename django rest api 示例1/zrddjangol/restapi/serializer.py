#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/1 11:48
# Author: zhourudong


from rest_framework import serializers
from .models import Book, Author, Publisher


class AuthorSerializer(serializers.Serializer):
    '''
        序列化models
    '''
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


"""
serializer 使用示例
content = '{"id":1,"first_name":"guang","last_name":"hongwei","email":"ibuler@qq.com"}'
from django.utils.six import BytesIO
data = content
from restapi.serializer import AuthorSerializer
from rest_framework.renderers import JSONRenderer
from restapi.models import Author
g = Author.objects.first()
g
Out[9]: <Author: Author object>
g
Out[10]: <Author: Author object>
g = Author.objects.first()
g
Out[12]: <Author: Author object>
s = AuthorSerializer(g) # 实例化
s
Out[14]: 
AuthorSerializer(<Author: Author object>):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    email = EmailField(allow_blank=True, max_length=100, required=False)
# 以上是实例内容
s.data
Out[16]: ReturnDict([('id', 1), ('name', '张三'), ('email', 'zhansan@qq.com')])
# 转换成json
JSONRenderer().render(s.data)
Out[18]: b'{"id":1,"name":"\xe5\xbc\xa0\xe4\xb8\x89","email":"zhansan@qq.com"}'
# bytes 类型的json字符串
# 将bytes 转换成字符串
c = JSONRenderer().render(s.data)
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
stream = BytesIO(c)
data = JSONParser().parse(stream)
data
Out[26]: {'email': 'zhansan@qq.com', 'id': 1, 'name': '张三'}
# -----------------------------------------------------------
ser = AuthorSerializer(data=data)
ser
Out[29]: 
AuthorSerializer(data={'name': '张三', 'id': 1, 'email': 'zhansan@qq.com'}):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100)
    email = EmailField(allow_blank=True, max_length=100, required=False)
ser.is_valid() # 校验是否合法
Out[30]: True
ser.validated_data()
Traceback (most recent call last):
  File "C:\3.5\lib\site-packages\IPython\core\interactiveshell.py", line 2847, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-31-3ba2bd51f4ab>", line 1, in <module>
    ser.validated_data()
TypeError: 'collections.OrderedDict' object is not callable
ser.validated_data
Out[32]: OrderedDict([('name', '张三'), ('email', 'zhansan@qq.com')])
ser.create(ser.validated_data)
Out[33]: <Author: Author object>



"""
