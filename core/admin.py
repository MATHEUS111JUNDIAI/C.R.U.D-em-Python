from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'valor')
    search_fields = ('nome_produto',)
    list_filter = ('valor',)
    ordering = ('nome_produto',)
