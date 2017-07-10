from django.db import models

from assets.models import Asset

__all__ = ['Project', ]


class Project(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='项目名')
    path = models.CharField(max_length=200, null=True, blank=True, verbose_name='项目路径')
    comment = models.CharField(max_length=256, default='', null=True, blank=True, verbose_name='项目备注')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    u_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    p_project = models.ForeignKey('self', related_name='f_project',blank=True, null=True, verbose_name='顶级项目')
    asset = models.ManyToManyField(Asset, blank=True,verbose_name='资产')

    class Meta:
        db_table = 'sh_project'



    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

