# Generated by Django 5.1.2 on 2024-11-06 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='observacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default=datetime.date(2024, 11, 13), verbose_name='Data de Devolução'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2024, 11, 6, 11, 46, 28, 119388, tzinfo=datetime.timezone.utc), verbose_name='Data do Empréstimo'),
        ),
    ]
