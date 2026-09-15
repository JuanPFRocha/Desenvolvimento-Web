from django.urls import path
from academico import views

urlpatterns = [
    path('listagem/professor/', views.ListagemProfessor, name='listagemProfessor'),
    path('adicionar/professor/', views.AdicionaProfessor, name='AdicionarProfessor'),
    path('deletar/professor/<id>', views.deletarprofessor, name='deletarProfessor'),
    path('editar/professor/<id>', views.editarProfessor, name='editarProfessor'),
    path('listagem/curso/', views.listagemCurso, name='listagemCurso'),
    path('adicionar/curso/', views.adicionarCurso, name='adicionarCurso'),
    path('editar/curso/<id>', views.editarCurso, name='editarCurso'),
    path('deletar/curso/<id>', views.deletarCurso, name='deletarCurso')

]