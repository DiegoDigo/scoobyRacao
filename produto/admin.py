from django.contrib import admin
from .models import Produto, Categoria, Animal


class AdminProduto(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria', 'animal']
    search_fields = ['nome', 'categoria__tipo', 'animal__tipo']
    list_filter = ['nome', 'categoria', 'animal']
    save_on_top = True

admin.site.register(Produto, AdminProduto)
admin.site.register(Categoria)
admin.site.register(Animal)
