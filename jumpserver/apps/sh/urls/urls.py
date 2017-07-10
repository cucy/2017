#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/25 11:28
# Author: zhourudong

from django.conf.urls import url, include

from sh import views

app_name = 'sh'

urlpatterns = [
    #  sh url配置
    # 主页面
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^zrd_test/$', views.index, name='zrd_test'),

    url(r'assert/', include([
        # 资产列表
        url(r'^$', views.AssertView.as_view(), name='assert'),
        # 修改资产信息
        url(r'modify_assert/$', views.AssertEditView.as_view(), name='modify_assert'),
    ])),

    url(r'project/',include([
        # 项目列表
        url(r'project/$', views.ProjectListView.as_view(), name='project_list'),
    ])),




]


