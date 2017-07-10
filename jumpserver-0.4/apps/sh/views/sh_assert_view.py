from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, View
from django.shortcuts import redirect
from django.urls import reverse

from assets.models import Asset
from sh.forms import AssetModelForm


__all__ = ['AssertView',  'AssertEditView']


# 资产列表
class AssertView(ListView):
    template_name = 'sh/assert/assert_list.html'
    model = Asset
    paginate_by = 10
    before_index = 6
    after_index = 5
    ordering = 'hostname'

    def get_context_data(self, **kwargs):
        context = super(AssertView, self).get_context_data(**kwargs)
        context['page_range'] = self.get_page_range(context['page_obj'])
        return context

    def get_page_range(self, page_obj):
        start_index = page_obj.number - self.before_index
        if start_index < 0:
            start_index = 0
        return page_obj.paginator.page_range[start_index: page_obj.number + self.after_index]


# 资产修改
class AssertEditView(TemplateView):
    template_name = 'sh/assert/modify_assert.html'

    def get_context_data(self, **kwargs):
        context = super(AssertEditView, self).get_context_data(**kwargs)
        # print(self.request.GET.get('asset', None))


        asset_obj_ = Asset.objects.filter(id=self.request.GET.get('asset', None)).first()
        # mf = AssetModelForm(instance=asset_obj_)
        context['asset_obj'] = asset_obj_

        # ProjectModelForm
        return context

    def post(self, request):
        # comment

        return redirect(reverse("sh:index"))


