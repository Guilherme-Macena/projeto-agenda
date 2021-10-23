from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao')  # atributos visiveis da classe

    list_display_links = ('id', 'nome')  # campos com link

    list_filter = ('nome', 'sobrenome')  # filtro

    search_fields = ('nome', 'sobrenome', 'telefone')  # pesquisar os campos


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
