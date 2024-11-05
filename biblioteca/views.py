from django.forms import HiddenInput
from django.shortcuts import redirect
from django.views.generic.list import ListView
from pages.models import Livro, Emprestimo
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class BibliotecaView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login') # apenas usuários logados acessam a biblioteca
    template_name = 'biblioteca/biblioteca.html'
    model = Livro # Listar elementos do meu banco de dados - nesse caso, os livros


class EmprestimoView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/form-emprestimo.html'
    model = Emprestimo
    fields = ['fk_livro','data_devolucao', 'fk_usuario', 'status' ] # a data de empréstimo é a data atual
    success_url = reverse_lazy('biblioteca')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Verificar se o usuário é superusuário
        if not self.request.user.is_staff:
            form.fields['fk_usuario'].widget.attrs['disabled'] = True
            form.fields['status'].widget.attrs['disabled'] = True
            form.fields['fk_usuario'].widget = HiddenInput()
            form.fields['status'].widget = HiddenInput()

        return form

    def form_valid(self, form):

        # automaticamente relaciona o usuário logado ao empréstimo
        form.instance.fk_usuario = self.request.user
        url = super().form_valid(form)

        return url


class HistoricoView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/historico-usuario.html'
    model = Emprestimo

    def get_queryset(self):
        # Lista apenas empréstimos do usuário logado
        self.object_list = Emprestimo.objects.filter(fk_usuario=self.request.user)
        return self.object_list
    

class AdmView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/admin-area.html'

    def test_func(self): # permite apenas superusers nessa página
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca') 
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)


class CadLivroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/cadastro-livros.html'
    model = Livro
    fields = ['titulo', 'autor', 'isbn', 'editora', 'ano_publicacao',
               'genero', 'quantidade_disponivel', 'descricao' ] 
    
    success_url = reverse_lazy('administrador')

    def test_func(self): # permite apenas superusers nessa página
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca') 
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)

class GestaoEmprestimosView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/gestao-emprestimos.html'
    model = Emprestimo

    def test_func(self): # permite apenas superusers nessa página
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca') 
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)


class EditarEmprestimoView(UpdateView):
    model = Emprestimo
    fields = ['id_emprestimo','fk_usuario', 'fk_livro', 'status', 'data_devolucao']
    template_name = 'edit-emprestimos'
    success_url = reverse_lazy('emprestimos')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        return form

    