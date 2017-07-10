#!/usr/bin/env python
# -- coding: utf-8 --
# Time: 2017/5/27 17:04
# Author: zhourudong

from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView

from sh.models import Project
from assets.models import Asset
from ..forms import ProjectModelForm

__all__ = ("ProjectListView",'index' )


class ProjectListView(ListView):
    # 项目列表

    template_name = 'sh/project/project_list.html'
    model = Project
    paginate_by = 10
    before_index = 6
    after_index = 5
    ordering = 'name'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        context['assert_obj']= Asset.objects.all()
        return context

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]

    def post(self,request):
        ret = {"status":0, 'errmsg': '添加项目成功'}
        print(request.POST.get('p_project'))
        post_data = ProjectModelForm(request.POST)
        if post_data.is_valid():
            # 数据通过检查 保存
            post_data.save()
        else:
            # import json
            ret["status"] = 1
            # ret["errmsg"] =  post_data.errors.as_json()
            # ret["errmsg"] = json.dumps({k: v[0] for k, v in post_data.errors.items()})
            # print(post_data.errors.as_json())
            # print( ret["errmsg"])
            err_msg ={k: v[0] for k, v in post_data.errors.items()}
            r_err_msg = ''
            for k,v in err_msg.items():
                r_err_msg +=k
                r_err_msg += ':'
                r_err_msg += v
                r_err_msg += ' '

            ret["errmsg"] = r_err_msg
        # print(obj.is_valid())
        # print(obj.errors.as_data())
        # print(request.POST)
        return JsonResponse(ret,safe=True)

# --------------- 测试 ----------------------------
def index(request):
    if request.method == 'GET':
        obj = ProjectModelForm()
        print(obj)
        return render(request, 'sh/zrd_test.html', {'obj':obj})
