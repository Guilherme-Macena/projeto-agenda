from django.shortcuts import render
from .models import Contato
# Create your views here.


def index(request):
    # variavel que recebe todos os objetos da class Contato
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
