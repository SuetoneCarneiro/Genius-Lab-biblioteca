from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'pages/index.html'

class BibliotecaPage(TemplateView):
    template_name = 'pages/biblioteca.html'
    