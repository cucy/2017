from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import AuthorModelForm
from .models import Author

__all__ = ['AuthorCreateView','AuthorDetailView', 'AuthorListView','AuthorUpdateView', 'AuthorDeleteView']


class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorModelForm
    success_url = reverse_lazy('author-list')
    template_name = 'author/author_form.html'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorModelForm
    template_name = 'author/author_form.html'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
    template_name = 'author/author_confirm_delete.html'
