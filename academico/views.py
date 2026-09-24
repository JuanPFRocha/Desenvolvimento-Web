from django.http import request
from django.shortcuts import redirect, render
from academico.models import Professor, Curso, Turma
from academico.forms import ProfessorForm, CursoForm

# Create your views here.
def listarProfessor(request):
    professores = Professor.objects.all()
    contexto = {
        'listaEst' : professores
    }
    return render(request, 'professores/listagem.html', contexto)

def criarProfessor(request):
    form  = ProfessorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listagemProfessor')
    dicionario = {
        'form' : form
    }
    return render(request, 'professor.html', dicionario)

def deletarProfessor(request, id=None):
    professor = Professor.objects.get(pk = id)
    professor.delete()
    return redirect('listagemProfessor')

def atualizarProfessor(request, id=None):
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
    return render(request, 'turmas/listagem.html', {'listaTurmas' : turmas})

def criarTurma(request):
    return render()

def deletarTurma(request):
    return render()

def atualizarTurma(request):
    return render()

def listarDisciplina(request):
    return render()
def criarDisciplina(request):
    return render()
def deletarDisciplina(request):
    return render()
def atualizarDisciplina(request):
    return render()

