from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *


class Home(ListView):
    model = NewsModel
    queryset = NewsModel.objects.all()[:3]
    context_object_name = 'news'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = NewsModel.objects.all()
        return context

