from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Contato(models.Model):
    # máximo de caracteres para o campo
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(
        max_length=255, blank=True)  # campo não obrigatório
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    # campo com uma data, importar pacotes.
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    # comparando uma tabela com a outra
    categoia = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
