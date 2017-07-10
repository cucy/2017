#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/7/7 10:22
# Author: zhourudong

import time

from configparser import ConfigParser
import paramiko


class ParamikoClient:
    def __init__(self, config_str, section):
        self.config = ConfigParser()
        self.config.read(config_str)

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp_client = None
        self.client_state = 0
        self.section = section
        self.shell = None

    def connect(self):
        try:
            self.client.connect(hostname=self.config.get(self.section, 'host'),
                                port=self.config.getint(self.section, 'port'),
                                username=self.config.get(self.section, 'username'),
                                password=self.config.get(self.section, 'password'),
                                timeout=self.config.getfloat(self.section, 'timeout'))
            self.client_state = 1

        except Exception as e:
            print(e.args)
            self.client.close()

    def run_cmd(self, cmd_str):
        stdin, stdout, stderr = self.client.exec_command(cmd_str)
        print(stdout.read())

    def get_sftp_client(self):
        if self.client_state == 0:
            self.connect()

        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())

        return self.sftp_client

    def multi_run_cmd(self, cmd_list):
        """
        解决问题
            串行执行命令环境（没有上下文联系）
                1、cd /tmp
                2、ls (返回的是用户的家目录而不是/tmp)

        :param cmd_list:
        :return:
        """
        if not self.shell:
            self.shell = self.client.invoke_shell(term='xterm')

        for cmd in cmd_list:
            print("do cmd {}".format(cmd))
            self.shell.send(cmd )  # 发送命令 (反斜线表示一行命令)
            time.sleep(0.5)
            receive_buf = self.shell.recv(1024)  # 返回的缓冲
            print('get comd return {}'.format(receive_buf))
