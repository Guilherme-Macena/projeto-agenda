from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    # variavel que recebe todos os objetos da class Contato
    # ordenado do ultimo para o primeiro id adicionado
    # filtrando pelo campo mostrar.
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )

    # criando paginação
    paginator = Paginator(contatos, 2)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # variavel que recebe o id class Contato, com tratamento de erro 404
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:  # Validação antes de mostrar contatodetalhado
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
