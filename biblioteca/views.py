from django.views.generic.list import ListView
from pages.models import Livro
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BibliotecaView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login') # apenas usuários logados acessam a biblioteca
    template_name = 'biblioteca/biblioteca.html'
    model = Livro # Listar elementos do meu banco de dados - nesse caso, os livros

class EmprestimoView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/form-emprestimo.html'


class HistoricoView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/historico-usuario.html'

class AdmView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/admin-area.html'

