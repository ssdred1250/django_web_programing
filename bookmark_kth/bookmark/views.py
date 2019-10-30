from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkList(ListView):
    model = Bookmark
    paginate_by = 2


class BookmarkAdd(CreateView):
    model = Bookmark
    fields = ['site_name', 'site_url']
    success_url = reverse_lazy('list')


class BookmarkDetail(DetailView):
    model = Bookmark


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'site_url']
    template_name_suffix = "_update"
    success_url = reverse_lazy('list')


class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')