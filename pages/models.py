from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    usuairo = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False)
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    telefone = models.CharField(max_length=22, verbose_name='Telefone')

    def __str__(self):
        return f'{self.nome_completo} - {self.email}'

class Livro(models.Model):
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    titulo = models.CharField(max_length=255, verbose_name='Título')
    autor = models.CharField(max_length=255, verbose_name='Autor')
    editora = models.CharField(max_length=255, verbose_name='Editora')
    ano_publicacao = models.DateField(verbose_name='Ano de Publicação')
    genero = models.CharField(max_length=100, verbose_name='Gênero')
    quantidade_disponivel = models.PositiveIntegerField(verbose_name='Quantidade Disponível')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return f'{self.titulo} - {self.autor}'


class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=20,
        choices=[('em_aberto', 'Em Aberto'), ('concluido', 'Concluído')],
        default='em_aberto',
        verbose_name='Status'
    )
    data_emprestimo = models.DateField(auto_now_add=True, verbose_name='Data do Empréstimo')
    data_devolucao = models.DateField(null=True, blank=True, verbose_name='Data de Devolução')
    fk_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    fk_livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name='Livro')

    def __str__(self):
        return f'Empréstimo {self.id_emprestimo} - {self.fk_usuario} - {self.status}'


class Contem(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, verbose_name='Empréstimo')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name='Livro')
    quantidade_emprestada = models.PositiveIntegerField(verbose_name='Quantidade emprestada')
