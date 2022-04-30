from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import *
from .models import *


class BaseView(TemplateView):
    template_name = "base.html"


class MainView(ListView):
    template_name = "main/index.html"
    model = Blog
    paginate_by = 5


class BioView(TemplateView):
    template_name = "main/bio.html"


class BlogView(DetailView):
    template_name = "main/blog.html"
    model = Blog


class ProdView(TemplateView):
    template_name = "main/prod.html"
