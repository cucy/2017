#!/bin/bash
#

/home/zhourudong/.pyenv/versions/3.5.2/envs/jumpserver3.5/bin/python  ../apps/manage.py makemigrations

/home/zhourudong/.pyenv/versions/3.5.2/envs/jumpserver3.5/bin/python ../apps/manage.py migrate
