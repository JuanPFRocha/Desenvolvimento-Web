from django.urls import path
from contas import views

urlpatterns = [
    path('registrar/', views.registrarUsuario, name='registrar_usuario'),
    path('login/', views.realizarLogin, name='login_usuario'),
    path('logout/', views.realizarLogout, name='logout_usuario')
]