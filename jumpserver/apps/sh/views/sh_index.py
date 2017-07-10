#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/6/1 17:00
# Author: zhourudong
import json
import datetime

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.http.request import QueryDict

from sh.models import Project
from assets.models import Asset
from ..forms import ProjectModelForm

__all__ = ['IndexView', ]


#  ztree数据(项目数据)
class zTree:
    def __init__(self):
        self.data = self.__get_product()

    def __get_product(self):
        return Project.objects.all()

    def __get_one_project(self):
        # 获取顶级项目
        return [p for p in self.data if not p.p_project_id]

    def __get_two_project(self, p_project):
        # 获取二级项目
        return [p for p in self.data if p.p_project_id == p_project]




    def get(self, async=False):
        ret = []
        for record in self.__get_one_project():
            tmp = self._get_ztree_attr(record)
            tmp['children'] = []
            for child in self.__get_two_project(record.id):
                tmp['children'].append(self._get_ztree_attr(child, async))
            ret.append(tmp)
        return ret

    def _get_ztree_attr(self, obj, async=False):
        ret = {"name": obj.name,
               "pid": 0 if obj.p_project_id is None else obj.p_project_id,
               "id": obj.id}
        if async:
            ret['isParent'] = True

        """
        返回数据格式:
                [
                    {
                        'children': [
                            {'id': 2, 'name': 'api', 'pid': 1},
                            {'id': 5, 'name': 'web移动端', 'pid': 1}
                        ],
                        'id': 1,
                        'name': 'web项目',
                        'pid': 0
                    },
                    {
                        'children': [
                            {'id': 4, 'name': 'python爬虫', 'pid': 3}
                        ],
                        'id': 3,
                        'name': '大数据项目',
                        'pid': 0
                    }
                ]
        """
        return ret


# 概览
class IndexView(TemplateView):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace',
                         'getoneinfo', 'postu']
    template_name = 'sh/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        ztree = zTree()
        data = ztree.get()
        context["ztree"] = json.dumps(data)
        # 所有资产列表
        context['all_assert_list'] = json.dumps(list(Asset.objects.all().values('id', 'hostname')))
        # 所有一级项目
        all_one_project = Project.objects.filter(p_project__isnull=True).values('id', 'name')
        context['all_one_project'] = json.dumps(list(all_one_project))
        return context

    def getoneinfo(self, request):
        ret = {"status": 0, "errmsg": ""}
        p_id = QueryDict(request.body)
        data = {}

        p_id = p_id.get('id')

        # 获取项目详情
        f_project = Project.objects.filter(id=p_id).values().first()
        now_time = datetime.datetime.now()
        if f_project:
            f_project['c_time'] = f_project.get('c_time', now_time).strftime('%Y-%m-%d %H:%M:%S')
            f_project['u_time'] = f_project.get('u_time', now_time).strftime('%Y-%m-%d %H:%M:%S')
            data.update(f_project)
        try:
            project = Project.objects.prefetch_related('asset').select_related('p_project').filter(id=p_id).first()
            all_one_project = Project.objects.filter(p_project__isnull=True).values('id', 'name')
        except Exception as e:
            ret['status'] = 2
            ret['errmsg'] = e.args

        # 一级项目名
        if project.p_project:
            data["pid"] = project.p_project.name
        else:
            data["pid"] = "顶级"

        # 该项目所有资产
        asset = {}
        if project.asset.all().exists():
            asset = list(project.asset.all().values('id','hostname','public_ip'))
        data['asset'] = asset
        data['all_one_project'] = list(all_one_project)  # 所有的顶级项目
        ret['data'] = data

        return JsonResponse(ret)

    def post(self, request):
        ret = {"status": 0, "errmsg": ""}
        print(request.POST)
        project_obj = Project.objects.filter(id=request.POST.get('id')).first()
        update_project = ProjectModelForm(request.POST, instance=project_obj)
        if update_project.is_valid():
            update_project.save()
        else:
            ret['status'] = 1
            err_msg = {k: v[0] for k, v in update_project.errors.items()}
            r_err_msg = ''
            for k, v in err_msg.items():
                r_err_msg += k
                r_err_msg += ':'
                r_err_msg += v
                r_err_msg += ' '
            ret["errmsg"] = r_err_msg

        return JsonResponse(ret)
