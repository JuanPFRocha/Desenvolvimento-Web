from django.contrib import admin
from academico.models import *
# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('matricula', 'nome', 'email', 'cpf')
class CursoAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nome', 'duracao', 'data_inicio', 'carga_horaria')
class TurmaAdmin(admin.ModelAdmin):
    list_display=('codigo', 'ano_ingresso', 'periodo')
class DisciplinaAdmin(admin.ModelAdmin):
    list_display=('codigo','nome', 'carga_horaria', 'turno')
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nome')

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
