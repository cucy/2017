#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/7 10:32
# Author: zhourudong

import time

from paramiko_client import ParamikoClient

if __name__ == '__main__':
    task_num = 1
    for i in range(task_num):
        section = 'ssh{}'.format(task_num)
        client = ParamikoClient("config.ini", section)
        client.connect()
        client.get_sftp_client().put("my_blog.tar.gz",
                                     "/home/ops_zhourudong/data/my_blog.tar.gz")

        cmd_list = ['cd /home/ops_zhourudong/data',
                    'pwd',
                    'tar xf /home/ops_zhourudong/data/my_blog.tar.gz  -C /home/ops_zhourudong/data',
                    'cd my_blog',
                    '/home/ops_zhourudong/.pyenv/versions/myblog27_13/bin/python -m pip install -r requiments.txt',
                    '/home/ops_zhourudong/.pyenv/versions/myblog27_13/bin/python manage.py runserver 192.168.1.58:9991'
                    ]
        client.multi_run_cmd(cmd_list)

    while True:
        time.sleep(0)

