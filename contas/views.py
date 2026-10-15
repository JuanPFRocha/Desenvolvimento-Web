from django.shortcuts import render
from contas.forms import FormularioRegistroUsuario
from contas.models import Usuario

def registrarUsuario(request):
    dados = FormularioRegistroUsuario(request.POST)
    if dados.is_valid():
        nome = dados.cleaned_data['nome']
        nomeUsuario = dados.cleaned_data['nomeUsuario']
        email = dados.cleaned_data['email']
        telefone = dados.cleaned_data['telefone']
        senha = dados.cleaned_data['senha']

        usuario = Usuario.objects.criarUsuario(nome=nome, nomeUsuario=nomeUsuario, telefone=telefone, email=email, senha=senha)
        usuario.save()

    else:
        dados - FormularioRegistroUsuario()

    context = {
        'formulario' : dados,
    }
    return render(request, 'contas/registrar.html', context)