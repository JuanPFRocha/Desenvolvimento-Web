from django import forms
from contas.models import Usuario

class FormularioRegistroUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'nomeUsuario', 'email', 'telefone']

    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o seu nome'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o seu E-mail'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Digite o telefone. Ex: (65) 99999-9999'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
