from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField()
    endereco = forms.CharField(
        max_length=255, required=False, label='Endereço')
    telefone = forms.CharField(max_length=22, required=False, label='Telefone')

    class Meta:
        model = User
        fields = ['username', 'email', 'endereco',
                  'telefone', 'password1', 'password2', 'is_staff']
