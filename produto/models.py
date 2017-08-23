from __future__ import unicode_literals
from django.db import models
from .querys import QuerySetProduto


class Animal(models.Model):
    tipo = models.CharField(u'Animal', max_length=100, unique=True)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


class Categoria(models.Model):
    tipo = models.CharField(u'categoria', max_length=100, unique=True)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Produto(models.Model):
    nome = models.CharField(u'Nome', max_length=50)
    descricao = models.CharField(u'Descrição', max_length=100)
    preco = models.DecimalField(u'Preço', max_digits=5, decimal_places=2)
    imagem = models.ImageField(u'Imagem', upload_to='img/produtos/')
    categoria = models.ForeignKey(u'categoria', Categoria)
    animal = models.ForeignKey(u'Animal', Animal)
    objects = QuerySetProduto.as_manager()

    def __str__(self):
        return self.nome

    class Meta:
        default_related_name = 'categorias'
        ordering = ['nome']
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
