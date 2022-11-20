from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from .models import User

class FormRegistro(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('cedula',)
    
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        qs = User.objects.filter(cedula=cedula)
        if qs.exists():
            raise forms.ValidationError("Cedula ya existente")
        return cedula
    
    def clean_password(self):
        password= self.cleaned_data.get("password")
        password2= self.cleaned_data.get("password2")
        if password and password2 and password!= password2:
            raise forms.ValidationError("Cedula ya existente")
        return password2

class AdminFormCrearUser(forms.ModelForm):
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('cedula', 'nombre', 'apellido', 'celular', 'foto',)
    
    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        qs = User.objects.filter(cedula=cedula)
        if qs.exists():
            raise forms.ValidationError("Cedula ya existente")
        return cedula
    
    def clean_password2(self):
        password1= self.cleaned_data.get("password1")
        password2= self.cleaned_data.get("password2")
        if password1 and password2 and password1!= password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
    def save(self, commit=True):
        user= super(AdminFormCrearUser, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class AdminFormActualizarUser(forms.ModelForm):
    password= ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('cedula', 'nombre', 'apellido', 'celular', 'foto', 'active', 'staff', 'admin')
    
    def clean_password(self):
        return self.initial['password']
