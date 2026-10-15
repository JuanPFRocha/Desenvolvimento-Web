from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from estudantes.forms import EstudanteForm
from estudantes.models import Estudante

# Arquivo para definir as regras de negócios

# Método/Função de listagem de estudantes

def atualizarEstudante(request, id=None):
    estudante = Estudante.objects.get(pk = id)
    form = EstudanteForm(request.POST or None, request.FILES or None, instance = estudante)
    if form.is_valid():
        form.save()
        return redirect('estudante_listar')
    dicionario = {
        'form' : form
    }
    return render(request, 'estudantes/atualizar.html', dicionario)

def listarEstudante(request):
    estudantes = Estudante.objects.all()
    contexto = {
        'listaEst' : estudantes,
    }
    return render(request, 'estudantes/listagem.html', contexto)

def criarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('estudante_listar')
    dicionario = {
        'form' : form
    }

    return render(request, 'estudantes/adicionar.html', dicionario)

def deletarEstudante(request, id=None):
    estudante = Estudante.objects.get(pk = id)
    estudante.delete()
    return redirect('estudante_listar')
