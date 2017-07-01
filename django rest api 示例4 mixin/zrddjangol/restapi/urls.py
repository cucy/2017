#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/1 11:52
# Author: zhourudong


from django.conf.urls import url
from  . import views
urlpatterns = [
    url(r'^athors/$',views.AuthorList.as_view(), name='author_lsit'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view(), name='author_detail'),
]