from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, identifier, password=None):
        if not identifier:
            raise ValueError('El usuario debe tener cedula')
        user = self.model(
            identifier=identifier
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def crete_staffuser(self, identifier, password):
        user = self.create_user(identifier, password= password,)
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, identifier, password):
        user = self.create_user(identifier, password=password,)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    identifier=models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    cellphone=models.CharField(max_length=10)
    picture=models.ImageField(upload_to='userPhoto')
    
    active=models.BooleanField( ('Activo'), default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD='identifier'
    REQUIRED_FIELDS= []
    def __str__(self):
        return str(self.identifier)
    
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

class Turn(models.Model):
    idTurn=models.CharField(max_length=4, unique=True)
    creation=models.DateTimeField(editable=False)
    state=models.CharField(max_length=10)
    user= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='patient')
    userStaff= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='userStaff', blank=True, editable=False)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.idTurn:
           self.creation = timezone.now()
        return super(Turn, self).save(*args, **kwargs)

