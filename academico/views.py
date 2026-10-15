from django.http import request
from django.shortcuts import redirect, render
from academico.models import Professor, Curso, Turma
from academico.forms import *

# Create your views here.
def listarProfessor(request):
    professores = Professor.objects.all()
    contexto = {
        'listaEst' : professores
    }
    return render(request, 'academico/professores/listagem.html', contexto)

def criarProfessor(request):
    form  = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('professor_listar')
    dicionario = {
        'form' : form
    }
    return render(request, 'academico/professores/adicionar.html', dicionario)

def deletarProfessor(request, id=None):
    professor = Professor.objects.get(pk = id)
    professor.delete()
    return redirect('professor_listar')

def atualizarProfessor(request, id=None):
    professor = Professor.objects.get(pk = id)
    form = ProfessorForm(request.POST or None, request.FILES or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('professor_listar')
    dicionario = {
        'form' : form
    }
    return render(request, 'academico/professores/atualizar.html', dicionario)


def listarCurso(request):
    cursos = Curso.objects.all()
    context = {
        'listCursos' : cursos
    }
    return render(request, 'cursos/listagem', context)

def criarCurso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagemCurso')
    dicionario = {
        'form' : form
    }
    return render(request, 'curso.html', dicionario)

def atualizarCurso(request, id=None):
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

def dashboard(request):
    return render(request, 'dashboard.html')

def listarTurma(request):
    turmas = Turma.objects.all()
    return render(request, 'academico/turmas/listagem.html', {'listaTurmas' : turmas})

def criarTurma(request):
    form = TurmaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('turma_listar')
    context = {
        'form' : form
    }
    return render(request, 'academico/turmas/adicionar.html', context)

def deletarTurma(request, codigo=None):
    turma = Turma.objects.get(pk =id)
    turma.delete()
    return redirect('turma_listar')

def atualizarTurma(request, codigo=None):
    turma = Turma.objects.get(pk = codigo)
    form = TurmaForm(request.POST or None, request.FILES or None, instance=turma)
    if form.is_valid():
        form.save()
        return redirect('turma_listar')
    return render(request, 'academico/turmas/atualizar.html', {'form' : form})

def listarDisciplina(request):
    return render()
def criarDisciplina(request):
    return render()
def deletarDisciplina(request):
    return render()
def atualizarDisciplina(request):
    return render()

