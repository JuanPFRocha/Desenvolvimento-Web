from django.db import models
from estudantes.models import Estudante

# Create your models here.
class Professor(models.Model):
    matricula = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    cpf = models.CharField(max_length=14)
    senha = models.CharField(max_length=16)
    foto = models.ImageField(upload_to='fotos/professores', null=True)
    def __str__(self):
            return self.nome


class Curso(models.Model):
    codigo = models.IntegerField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/cursos')
    duracao = models.DecimalField(max_digits=3, decimal_places=2)
    data_inicio = models.DateField(blank=True)
    carga_horaria = models.IntegerField(max_length=2)
    professor = models.ManyToManyField(Professor, blank=True)
    def __str__(self):
            return self.nome 


class Turma(models.Model):
    codigo = models.CharField(max_length=15)
    ano_ingresso = models.IntegerField(max_length=4)
    periodo = models.IntegerField(max_length=1)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    def __str__(self):
         return self.codigo

class Disciplina(models.Model):
    codigo = models.IntegerField(max_length=3)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(max_length=2)
    turno = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    estudante = models.ManyToManyField(Estudante, blank=True)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
     codigo = models.CharField(max_length=10)
     nome = models.CharField(max_length=100)
     imagem = models.ImageField(upload_to='fotos/cursos')