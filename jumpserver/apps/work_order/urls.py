#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/12 10:49
# Author: zhourudong


from django.conf.urls import url
from . import views

urlpatterns = [
    # 工单列表
    url(r'apply/$', views.WorkOrderApplyView.as_view(), name='apply'),
    url('^list/$', views.WorkOrderListView.as_view(), name='list'),
    url('^detail/$', views.WorkOrderDetailView.as_view(), name='detail'),
    url('^history/$', views.WorkOrderHistoryView.as_view(), name='history'),
]
