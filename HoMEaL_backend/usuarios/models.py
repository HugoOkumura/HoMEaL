from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UsuarioManager(BaseUserManager):


    '''
    Como esta usando uma classe customizada pra User é necessário a criação de um Manager para permitir autenticação e o 
    utilizo dos campos username e password do User.
    '''
    def create_user(self, email, password=None, tipo_usuario='cliente'):
        if not email:
            raise ValueError('O usuário deve ter um email')
        usuario = self.model(email=email, tipo_usuario=tipo_usuario)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(email, password, tipo_usuario='gerente')
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario


class CamposComuns(models.Model):

    '''
    Classe puramente para evitar repetição dos campos dos usuários
    '''
    nome = models.CharField(max_length=30, unique=True)
    endereco = models.CharField(max_length=70, blank=True)
    cpf = models.CharField(max_length=11, unique=True)

    class Meta:
        abstract = True

class Usuario(AbstractBaseUser):

    '''
    Classe abstrata de Usuario a partir desta classe que poderá ser feita a autenticação e ver o tipo de usuário (Cliente/Gerente)
    '''

    TIPO_USUARIO_CHOICES = [
        ("gerente","Gerente"),
        ("cliente","Cliente")
    ]
    email = models.CharField(max_length=50, unique=True)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, default='cliente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        

class Cliente(CamposComuns):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='cliente')
    # resto dos campos

class Gerente(CamposComuns):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='gerente')
    #resto dos campos
    data_inicio = models.DateTimeField(default=timezone.now)
    ainda_trabalha = models.BooleanField(default=True)
    data_final = models.DateField(blank=True, null=True)