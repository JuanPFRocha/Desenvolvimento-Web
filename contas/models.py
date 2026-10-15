from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class GerenciamentoUsuario(BaseUserManager):
    def criarUsuario(self, nome, nomeUsuario, telefone, email, senha=None):
        if not email:
            return ValueError('usuário deve ter um email.')
        if not nomeUsuario:
            return ValueError('o campo nome de usuário deve ser informado.')
        usuario = self.model(
            email = self.normalize_email(email),
            nomeUsuario = nomeUsuario,
            nome = nome,
            telefone = telefone,
        )
        usuario.set_password(senha)
        usuario.save(using=self._db)

        return usuario



class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=150)
    nomeUsuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    telefone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'email', 'telefone']

    objects = GerenciamentoUsuario()

