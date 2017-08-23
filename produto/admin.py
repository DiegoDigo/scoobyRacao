from django.contrib import admin
from .models import Produto, Categoria, Animal


class AdminProduto(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria', 'animal']

admin.site.register(Produto, AdminProduto)
admin.site.register(Categoria)
admin.site.register(Animal)
