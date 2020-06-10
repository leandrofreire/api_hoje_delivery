from django.contrib import admin

from .models import Categoria, Loja, Categoria_produto, Produto

class LojaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria_loja', 'descricao']
    search_fields = ['nome', 'categoria_loja', 'descricao']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'loja', 'categoria']
    search_fields = ['nome', 'categoria', 'loja']

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Loja, LojaAdmin)
admin.site.register(Categoria_produto)
admin.site.register(Produto, ProductAdmin)