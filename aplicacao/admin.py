from django.contrib import admin
from aplicacao.models import Produtos, Marca


class Produto(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo', 'valor', 'validade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Produtos, Produto)


class Marcas(admin.ModelAdmin):
    list_display = ('id', 'nome_marca', 'slogan', 'tipo')
    list_display_links = ('id', 'nome_marca')
    search_fields = ('nome_marca',)
    list_per_page = 20


admin.site.register(Marca, Marcas)
