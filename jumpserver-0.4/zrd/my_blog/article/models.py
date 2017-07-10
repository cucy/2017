# -*- coding: utf-8 -*-
from django.db import models


# 保存配置信息
class SSHInfo(models.Model):
    host_name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=22)
    usr = models.CharField(max_length=50)
    pwd = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.host_name
