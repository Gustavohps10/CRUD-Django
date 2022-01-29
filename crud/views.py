from django.shortcuts import render, redirect
from .models import Categoria, Jogo
from django.shortcuts import get_object_or_404
from .forms import *

def listarJogos(request, rotuloCategoria=None, result=None):
    categoria = None
    categorias = Categoria.objects.all()
    jogosLimit = Jogo.objects.all().order_by('-id')[:5]
    jogos = Jogo.objects.all()
    search = request.GET.get('search')

    if search:
        jogos = Jogo.objects.filter(nome__icontains=search)
        result = search

    if rotuloCategoria:
        categoria = get_object_or_404(Categoria, rotulo=rotuloCategoria)
        jogos = jogos.filter(categoria=categoria)
        
    return render(request, 'crud/jogo/lista-jogo.html', {'categoria':categoria, 'categorias':categorias, 'jogos':jogos, 'jogosLimit': jogosLimit, "result": result})

def listarCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'crud/jogo/lista-categoria.html',{'categorias':categorias })

def detalharJogo(request, id, rotulo):
    jogo = get_object_or_404(Jogo, id=id, rotulo=rotulo)
    return render(request, 'crud/jogo/detalhes-jogo.html',{'jogo':jogo})

def cadastrarJogo(request):
    formName = "CADASTRAR JOGO"
    form = FormularioJogo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('crud:listarJogos')
    return render(request, 'crud/jogo/cadastrar-jogo.html', {'form':form, "formName":formName})

def cadastrarCategoria(request):
    formName = "CADASTRAR CATEGORIA"
    form = FormularioCategoria(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud:listarCategorias')
    return render(request, 'crud/jogo/cadastrar-categoria.html', {'form':form, "formName":formName})

def deletarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    categoria.delete()
    categorias = Categoria.objects.all()
    return render(request, 'crud/jogo/lista-categoria.html',{'categorias':categorias })

def deletarJogo(request, id):
    if Jogo.objects.filter(id = id).exists():
        jogo = Jogo.objects.get(id = id)
        jogo.delete()
    return redirect('crud:listarJogos')


def editarCategoria(request, id):
    formName = "EDITAR CATEGORIA"
    categoria = Categoria.objects.get(id = id)
    formulario = FormularioCategoria(request.POST or None, instance=categoria)
    if formulario.is_valid():
        formulario.save()
        return redirect('crud:listarCategorias')
    return render(request, 'crud/jogo/cadastrar-categoria.html', {'form':formulario, "formName":formName})

def editarJogo(request, id):
    formName = "EDITAR JOGO"
    if Jogo.objects.filter(id = id).exists():
        jogo = Jogo.objects.get(id = id)
    else:
        return redirect('crud:listarJogos')
    form = FormularioJogo(request.POST or None, request.FILES or None,instance=jogo)
    if form.is_valid():
        form.save()
        return redirect('crud:listarJogos')
    return render(request, 'crud/jogo/cadastrar-jogo.html', {'form':form, "formName":formName})