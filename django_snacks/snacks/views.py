from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeViews(TemplateView):
    template_name = 'home.html'


class AboutViews(TemplateView):
    template_name = 'about.html'
