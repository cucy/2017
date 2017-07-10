#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/12 10:25
# Author: zhourudong

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin:
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)