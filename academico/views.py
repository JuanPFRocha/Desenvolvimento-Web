from django.http import request
from django.shortcuts import redirect, render
from academico.models import Professor
from academico.forms import ProfessorForm

# Create your views here.
def ListagemProfessor(request):
    professores = Professor.objects.all()
    contexto = {
        'listaEst' : professores
    }
    return render(request, 'listagemProfessor.html', contexto)

def AdicionaProfessor(request):
    form  = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagemProfessor')
    dicionario = {
        'form' : form
    }
    return render(request, 'professor.html', dicionario)

def deletarprofessor(request, id=None):
    professor = Professor.objects.get(pk = id)
    professor.delete()
    return redirect('listagemProfessor')

def editarProfessor(request, id=None):
    professor = Professor.objects.get(pk = id)
    form = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ListagemProfessor')
    else:
        form = ProfessorForm(instance=professor)
    dicionario = {
        'form' : form
    }
    return render(request, 'editarProfessor.html', dicionario)
