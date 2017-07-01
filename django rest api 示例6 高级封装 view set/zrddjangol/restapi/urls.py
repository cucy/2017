#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/1 11:52
# Author: zhourudong

from django.conf.urls import url, include
from . import views

## version 2
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('authors',views.AuthorViewSet)
urlpatterns = [
    url(r'^',include(router.urls)),
]

'''
## version 1

author_list = AuthorViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

author_detail = AuthorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns += [
    url(r'^authors/$', author_list, name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$', author_detail, name='author-detail'),
]

'''
