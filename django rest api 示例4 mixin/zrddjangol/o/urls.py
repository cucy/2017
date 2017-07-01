#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/30 14:37
# Author: zhourudong

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'author/add/$', views.AuthorCreateView.as_view(), name='author-add'),
    url(r'author/list/$', views.AuthorListView.as_view(), name='author-list'),
    url(r'author/(?P<pk>\d+)/detail/$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'author/(?P<pk>\d+)/update/$', views.AuthorUpdateView.as_view(), name='author-update'),
    url(r'author/(?P<pk>\d+)/delete/$', views.AuthorDeleteView.as_view(), name='author-delete'),

]
