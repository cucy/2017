#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/31 11:48
# Author: zhourudong

from django.forms import ModelForm

from sh.models import Project
from assets.models import Asset


__all__ = ["ProjectModelForm",'AssetModelForm' ]

class ProjectModelForm(ModelForm):



    class Meta:
        model = Project
        fields = '__all__'

    def clean_p_project(self):
        new_p_project = self.cleaned_data.get('p_project', None)
        # 检查是否是顶级项目
        if str(new_p_project) == 'None':
            new_p_project = None
        return new_p_project

class AssetModelForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        #field_classes =
