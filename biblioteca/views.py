from django.shortcuts import render
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BibliotecaView(LoginRequiredMixin ,TemplateView):
    login_url = reverse_lazy('login') # apenas usuários logados acessam a biblioteca
    template_name = 'biblioteca/biblioteca.html'