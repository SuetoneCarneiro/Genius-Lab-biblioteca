# Generated by Django 5.1.2 on 2024-11-06 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_emprestimo_observacoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2024, 11, 6, 11, 46, 30, 807803, tzinfo=datetime.timezone.utc), verbose_name='Data do Empréstimo'),
        ),
    ]
