from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *


class Home(ListView):
    model = ServiceModel
    queryset = ServiceModel.objects.all()
    context_object_name = 'service'
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news'] = ServiceModel.objects.all()
    #     return context


class Service(ListView):
    model = ServiceModel
    queryset = ServiceModel.objects.all()
    context_object_name = 'service'
    template_name = 'service.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news'] = ServiceModel.objects.all()
    #     return context



class About(ListView):
    model = ServiceModel
    queryset = ServiceModel.objects.all()
    context_object_name = 'service'
    template_name = 'about.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news'] = ServiceModel.objects.all()
    #     return context



class Contact(ListView):
    model = ServiceModel
    queryset = ServiceModel.objects.all()
    context_object_name = 'service'
    template_name = 'contact.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news'] = ServiceModel.objects.all()
    #     return context

