# Generated by Django 5.1.2 on 2024-11-05 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_emprestimo_data_devolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(default=datetime.date(2024, 11, 12), verbose_name='Data de Devolução'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2024, 11, 5, 18, 23, 56, 453691, tzinfo=datetime.timezone.utc), verbose_name='Data do Empréstimo'),
        ),
    ]
