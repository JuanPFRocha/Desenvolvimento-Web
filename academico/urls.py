from django.urls import path
from academico import views

urlpatterns = [
    path('listagem/professor/', views.ListagemProfessor, name='listagemProfessor'),
    path('adicionar/professor/', views.AdicionaProfessor, name='AdicionarProfessor'),
    path('deletar/professor/<id>', views.deletarprofessor, name='deletarProfessor'),
    path('editar/professor/<id>', views.editarProfessor, name='editarProfessor'),


]