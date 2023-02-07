from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Loja)
admin.site.register(Endereco)
admin.site.register(Cliente)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'preco', 'estoque',
                    'disponivel', 'data_criacao', 'data_ultima_atualizacao']
    list_filter = ['disponivel', 'data_criacao', 'data_ultima_atualizacao']
    list_editable = ['preco', 'estoque', 'disponivel']
    prepopulated_fields = {'slug': ('nome',)}
