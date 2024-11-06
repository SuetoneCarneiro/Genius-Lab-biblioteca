from django.contrib import messages
from django.forms import HiddenInput
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from biblioteca.forms import RelatorioFiltroForm
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
    fields = ['fk_livro', 'data_emprestimo','data_devolucao', 'fk_usuario', 'status' ] # a data de empréstimo é a data atual
    success_url = reverse_lazy('biblioteca')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Verificar se o usuário é superusuário
        if not self.request.user.is_staff:
            # fk_usuario e status automaticamente atreladas ao usuário logado
            form.instance.fk_usuario = self.request.user
            form.instance.status = 'solicitado'

            # ocultando fk_usuario e status para usuários comuns
            form.fields['fk_usuario'].widget = HiddenInput()
            form.fields['status'].widget = HiddenInput()

            # Campos ocultos tenham os valores certos
            form.fields['fk_usuario'].initial = self.request.user
            form.fields['status'].initial = 'solicitado'

        livro_id = self.request.GET.get('livro_id')
        if livro_id:
            livro = get_object_or_404(Livro, id=livro_id)
            form.instance.fk_livro = livro
            form.fields['fk_livro'].initial = livro

        return form

    def form_valid(self, form):
        # Verifica se os valores dos campos ocultos estão definidos
        if not form.instance.fk_usuario:
            form.instance.fk_usuario = self.request.user
        if not form.instance.status:
            form.instance.status = 'solicitado'


        # Lógica para diminuir 1 livro quando for solicitado o empréstimo

        livro = form.cleaned_data['fk_livro']

        # Verificar se há exemplares disponíveis
        if livro.quantidade_disponivel <= 0:
            messages.error(self.request, "não há exemplares disponíveis para empréstimo.")
            return redirect('emprestimo')  # Redireciona para a página do formulário
        
        # Reduz a quantidade disponível
        livro.quantidade_disponivel -= 1
        livro.save()  # Salva a alteração no banco de dados

        # formulário válido -> salva o empréstimo
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
    
    success_url = reverse_lazy('biblioteca')

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


class EditarEmprestimoView(UserPassesTestMixin,UpdateView):
    model = Emprestimo
    fields = ['id_emprestimo','fk_usuario', 'fk_livro', 'status','data_devolucao', 'observacoes']
    template_name = 'edit-emprestimos'
    success_url = reverse_lazy('emprestimos')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        return form
    
    def form_valid(self, form):
        # Obtém o objeto de empréstimo atual antes de salvar o novo status
        emprestimo = self.get_object()
        livro = emprestimo.fk_livro

        # Verifica se o status foi alterado para "concluído"
        if form.cleaned_data['status'] == 'concluido' and emprestimo.status != 'concluido':
            # Soma 1 à quantidade disponível do livro
            livro.quantidade_disponivel += 1
            livro.save()  # Salva a alteração no banco de dados
            messages.success(self.request, f"Empréstimo {emprestimo.id_emprestimo} concluído. Livro devolvido com sucesso.")

        return super().form_valid(form)
    
    def test_func(self): # permite apenas superusers nessa página
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca') 
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)

    
class RelatoriosView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    login_url = reverse_lazy('login')
    template_name= 'biblioteca/relatorios.html'
    model = Emprestimo
    context_object_name = 'emprestimos'

    def test_func(self): # permite apenas superusers nessa página
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca') 
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)
        
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = RelatorioFiltroForm(self.request.GET)
        
        if self.form.is_valid():
            data_inicio = self.form.cleaned_data.get('data_inicio')
            data_fim = self.form.cleaned_data.get('data_fim')
            status = self.form.cleaned_data.get('status')

            # Filtro por data
            if data_inicio:
                queryset = queryset.filter(data_emprestimo__gte=data_inicio)
            if data_fim:
                queryset = queryset.filter(data_emprestimo__lte=data_fim)
            
            # Filtro por status
            if status:
                queryset = queryset.filter(status=status)
                
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context
    
