from django.urls import path
from .views import BibliotecaView, EmprestimoView, HistoricoView, AdmView, CadLivroView
from .views import GestaoEmprestimosView, EditarEmprestimoView, RelatoriosView

urlpatterns = [
    path('biblioteca/', BibliotecaView.as_view(
        template_name='biblioteca/biblioteca.html'), name='biblioteca'),
    path('emprestimo/', EmprestimoView.as_view(
        template_name='biblioteca/form-emprestimo.html'), name='emprestimo'),
    path('historico/', HistoricoView.as_view(
        template_name='biblioteca/historico-usuario.html'), name='historico'),
    path('administrador/', AdmView.as_view(template_name='biblioteca/admin-area.html'),
         name='administracao'),
    path('cadastrar-livro/', CadLivroView.as_view(
        template_name='biblioteca/cadastro-livros.html'), name='cadastrar-livro'),
    path('emprestimos/', GestaoEmprestimosView.as_view(
        template_name='biblioteca/gestao-emprestimos.html'), name='emprestimos'),
    path('editar/<int:pk>', EditarEmprestimoView.as_view(
        template_name='biblioteca/edit-emprestimos.html'), name='editar'),
    path('relatorios/', RelatoriosView.as_view(
        template_name='biblioteca/relatorios.html'), name='relatorios'),

]
