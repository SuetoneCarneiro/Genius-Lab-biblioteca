# Generated by Django 5.1.2 on 2024-11-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_livro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.CharField(choices=[('solicitado', 'Solicitado'), ('em_aberto', 'Em Aberto'), ('concluido', 'Concluído')], default='solicitado', max_length=20, verbose_name='Status'),
        ),
    ]
