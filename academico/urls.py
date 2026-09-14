from django.urls import path
from academico import views

urlpatterns = [
    path('listagem/', views.ListagemProfessor, name='listagemProfessor'),
    path('adicionar/', views.AdicionaProfessor, name='AdicionarProfessor'),
    path('deletar/<id>', views.deletarprofessor, name='deletarProfessor'),
    path('editar/<id>', views.editarProfessor, name='editarProfessor')
]