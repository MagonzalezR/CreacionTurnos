from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cedula=models.IntegerField(primary_key=True)
    USERNAME_FIELD='cedula'
    celular=models.CharField(max_length=10)
    foto=models.ImageField(upload_to='gestionTurnos/fotos')

class Turno(models.Model):
    numero_urno=models.CharField(max_length=4)
    hora_creacion=models.DateField()
    estado=models.CharField(max_length=10)
    usuario= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='usuarioTurno')
    usuario_staff= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='usuarioStaff')

