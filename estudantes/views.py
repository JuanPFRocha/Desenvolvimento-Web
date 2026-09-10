from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from estudantes.forms import EstudanteForm
from estudantes.models import Estudante

# Arquivo para definir as regras de negócios

# Método/Função de listagem de estudantes

def editarEstudante(request, id=None):
    estudante = Estudante.objects.get(pk = id)
    form = EstudanteForm(request.POST or None, request.FILES or None, instance = estudante)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = EstudanteForm(instance=estudante)

    dicionario = {
        'form' : form
    }
    return render(request, 'editar.html', dicionario)

def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    contexto = {
        'listaEst' : estudantes,
    }
    return render(request, 'listagem.html', contexto)

def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    dicionario = {
        'form' : form
    }

    return render(request, 'estudante.html', dicionario)

def deletarEstudante(request, id=None):
    estudante = Estudante.objects.get(pk = id)
    estudante.delete()
    return redirect('/')
