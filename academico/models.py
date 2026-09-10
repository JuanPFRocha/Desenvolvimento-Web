from django.db import models

# Create your models here.
class Professor(models.Models):
    matricula = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    cpf = models.CharField(max_length=14)

class Curso(models.Models):
    codigo = models.IntegerField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/cursos')
    duracao = models.DecimalField(max_digits=3, decimal_places=2)
    data_inicio = models.DateField(blank=True)
    carga_horaria = models.IntegerField(max_length=2)

class Turma(models.Models):
    codigo = models.CharField(max_length=15)
    ano_ingresso = models.IntegerField(max_length=4)
    periodo = models.IntegerField(max_length=1)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

class Disciplina(models.Models):
    codigo = models.IntegerField(max_length=3)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(max_length=2)
    turno = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

