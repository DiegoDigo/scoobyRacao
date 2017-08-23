# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import produto.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, unique=True, verbose_name='Animal')),
            ],
            options={
                'verbose_name': 'Animal',
                'ordering': ['tipo'],
                'verbose_name_plural': 'Animais',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, unique=True, verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['tipo'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('imagem', models.ImageField(upload_to='img/produtos/', verbose_name='Imagem')),
                ('animal', models.ForeignKey(on_delete=produto.models.Animal, related_name='categorias', to='produto.Animal')),
                ('categoria', models.ForeignKey(on_delete=produto.models.Categoria, related_name='categorias', to='produto.Categoria')),
            ],
            options={
                'default_related_name': 'categorias',
                'verbose_name': 'Produto',
                'ordering': ['nome'],
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
