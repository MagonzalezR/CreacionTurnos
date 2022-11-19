from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
class ManejadorUser(BaseUserManager):
    def create_user(self, cedula, password=None):
        if not cedula:
            raise ValueError('El usuario debe tener cedula')
        usuario = self.model(
            cedula=cedula
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def crete_staffuser(self, cedula, password):
        usuario = self.create_user(cedula, password= password,)
        usuario.staff = True
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, cedula, password):
        usuario = self.create_user(cedula, password=password,)
        usuario.staff = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario

class User(AbstractBaseUser):
    cedula=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    celular=models.CharField(max_length=10)
    foto=models.ImageField(upload_to='userPhoto')
    
    active=models.BooleanField( ('Activo'), default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)

    objects = ManejadorUser()


    USERNAME_FIELD='cedula'
    REQUIRED_FIELDS= []
    def __str__(self):
        return str(self.cedula)
    
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_superuser(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin
    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

class Turno(models.Model):
    numero_urno=models.CharField(max_length=4)
    hora_creacion=models.DateTimeField(editable=False)
    estado=models.CharField(max_length=10)
    usuario= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='usuarioTurno')
    usuario_staff= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='usuarioStaff', blank=True, editable=False)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
           self.hora_creacion = timezone.now()
        return super(Turno, self).save(*args, **kwargs)

