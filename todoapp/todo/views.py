# from msilib.schema import ListView
from dataclasses import field
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from todo.models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    fields = ('title', 'memo')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    fields = ('title', 'memo')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')