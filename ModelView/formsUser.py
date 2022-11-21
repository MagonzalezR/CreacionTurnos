from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from .models import User

class FormRegistration(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('identifier',)
    
    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        qs = User.objects.filter(identifier=identifier)
        if qs.exists():
            raise forms.ValidationError("identifier ya existente")
        return identifier
    
    def clean_password(self):
        password= self.cleaned_data.get("password")
        password2= self.cleaned_data.get("password2")
        if password and password2 and password!= password2:
            raise forms.ValidationError("Passwords distintas")
        return password2

class AdminFormCreateUser(forms.ModelForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('identifier', 'name', 'lastName', 'cellphone', 'picture',)
    
    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        qs = User.objects.filter(identifier=identifier)
        if qs.exists():
            raise forms.ValidationError("identifier ya existente")
        return identifier
    
    def clean_password2(self):
        password1= self.cleaned_data.get("password1")
        password2= self.cleaned_data.get("password2")
        if password1 and password2 and password1!= password2:
            raise forms.ValidationError("Las passwords no coinciden")
        return password2
    
    def save(self, commit=True):
        user= super(AdminFormCreateUser, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class AdminFormUpdateUser(forms.ModelForm):
    password= ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('identifier', 'name', 'lastName', 'cellphone', 'picture', 'active', 'staff', 'admin')
    
    def clean_password(self):
        return self.initial['password']
