#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/1 11:52
# Author: zhourudong


from django.conf.urls import url
from  . import views
urlpatterns = [
    url(r'^athors/$',views.author_list, name='author_lsit'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.author_detail, name='author_detail'),
]