from django.shortcuts import render, get_object_or_404
from .models import Contato
# Create your views here.


def index(request):
    # variavel que recebe todos os objetos da class Contato
    contatos = Contato.objects.all()

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # variavel que recebe o id class Contato, com tratamento de erro 404
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
