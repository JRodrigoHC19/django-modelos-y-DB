from django.shortcuts import render

# Create your views here.
from .models import Entrada, Autor


def list_entradas(request, autor):
    entradas = Entrada.objects.filter(autor__nombre=autor)
    return render(request, 'blog/lista_entradas.html', {'entradas':entradas, 'autor':autor})

def index(request):
    autores = Autor.objects.all()
    return render(request, 'blog/principal.html', {'autores': autores})