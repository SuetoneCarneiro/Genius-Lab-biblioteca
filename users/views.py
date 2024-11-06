from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UsuarioForm
# Create your views here.


class CadUsuarioView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'biblioteca/cadastro-usuarios.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('biblioteca')

    def test_func(self):  # permite apenas superusers nessa página
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Redireciona o usuário para a biblioteca, caso esteja logado
        if self.request.user.is_authenticated:
            return redirect('biblioteca')
        else:
            # se não estiver logado, redireciona para login
            return redirect(self.login_url)
