#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/7 16:00
# Author: zhourudong

from fabric.api import run

def hello():
    print("hello ")

def test(a):
    print('test{}'.format(a))

def host_type():
    run('date')