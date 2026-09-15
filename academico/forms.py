from django import forms
from .models import Professor, Curso

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'