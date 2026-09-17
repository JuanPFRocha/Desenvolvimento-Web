from django.contrib import admin
from estudantes.models import Estudante

# Register your models here.
class EstudanteAdmin(admin.ModelAdmin):
    list_display=('matricula', 'nome', 'telefone', 'email', 'nascimento')

admin.site.register(Estudante, EstudanteAdmin)
