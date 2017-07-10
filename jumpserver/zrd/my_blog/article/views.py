# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from models import SSHInfo

# Create your views here.
try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser
try:
    import paramiko_client
except:
    from . import paramiko_client


def home(request):
    # 如果请求里有file
    for key in request.FILES:
        file = request.FILES[key]
        config = ConfigParser()  # 读取配置文件
        config.readfp(file)
        for section in config.sections():
            print(section)
            host_name = config.get(section, 'host_name')
            host = config.get(section, 'host')
            port = config.get(section, 'port')
            usr = config.get(section, 'username')
            pwd = config.get(section, 'password')
            new_ssh, create = SSHInfo.objects.update_or_create(
                host_name=host_name
                , host=host
                , port=port
                , usr=usr
                , pwd=pwd
            )
            new_ssh.save() # 保存配置信息到数据库
    sshs = SSHInfo.objects.all() # 获取所有对象
    if len(sshs) > 0:
        return render_to_response('sshlist.html', {'sshs': sshs})
    else:
        return render_to_response('home_view.html')


def run_ssh_cmd(requset):
    # 获取所有的信息
    sshs = SSHInfo.objects.all()

    cmd_res = {}
    for ssh in sshs:
        client = paramiko_client.ParamikoClient()
        client.connect(ssh)
        res = client.run_cmd('date') # 执行命令 接收返回
        cmd_res[ssh.host_name] = res

    return render_to_response('cmd_res.html', {'cmd_res': cmd_res})
