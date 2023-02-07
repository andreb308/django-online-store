from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Loja)
admin.site.register(Endereco)
admin.site.register(Cliente)
