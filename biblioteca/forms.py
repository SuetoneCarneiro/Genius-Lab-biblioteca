# Esse formulário vai servir apenas para criar os filtros na página relatorios.html
from django import forms

class RelatorioFiltroForm(forms.Form):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Início",
        required=False
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Fim",
        required=False
    )
    status = forms.ChoiceField(
        choices=[('', 'Todos'), ('solicitado', 'Solicitado'),('em_aberto', 'Em Aberto'), ('concluido', 'Concluído')],
        label="Status",
        required=False
    )
