#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/30 15:33
# Author: zhourudong

from django import forms
from .models import Author


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"