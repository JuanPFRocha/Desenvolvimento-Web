from django.http import request
from django.shortcuts import redirect, render
from academico.models import Professor, Curso
from academico.forms import ProfessorForm, CursoForm

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
    form = ProfessorForm(request.POST or None, request.FILES or None, instance= professor)
    if form.is_valid():
        form.save()
        return redirect('listagemProfessor')
    else:
        form = ProfessorForm(instance=professor)
    dicionario = {
        'form' : form
    }
    return render(request, 'editarProfessor.html', dicionario)

def listagemCurso(request):
    cursos = Curso.objects.all()
    context = {
        'listaEst' : cursos 
    }
    return render(request, 'listagemCurso.html ', context)

def adicionarCurso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagemCurso')
    dicionario = {
        'form' : form
    }
    return render(request, 'curso.html', dicionario)

def editarCurso(request, id=None):
    curso = Curso.objects.get(pk = id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=Curso)
    if form.is_valid():
        form.save()
        return redirect('listagemCurso')
    else:
        form = CursoForm(instance=Curso)
    dicionario = {
        'form' : form
    }
    return render(request, 'editarCurso.html', dicionario)

def deletarCurso(request, id=None):
    curso = Curso.objects.get(pk = id)
    curso.delete()
    return redirect('listagemCurso')