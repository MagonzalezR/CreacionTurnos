from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Turno
from .forms import AdminFormActualizarUser, AdminFormCrearUser

class CustomUserAdmin(UserAdmin):
    form = AdminFormActualizarUser
    add_form = AdminFormCrearUser

    list_display = ('cedula','nombre', 'staff', 'celular',)
    list_filter = ('cedula','nombre', 'staff', 'celular',)
    fieldsets = (
        (None, {'fields': ('cedula', 'password','nombre','apellido', 'celular', 'foto')}),
        ('Permissions', {'fields': ('staff', 'active', 'admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cedula','nombre','apellido', 'celular', 'foto', 'password1', 'password2', 'staff', 'active', 'admin')}
        ),
    )
    search_fields = ('cedula',)
    ordering = ('cedula',)
    filter_horizontal= ()

class TurnoAdmin(admin.ModelAdmin):
    model=Turno
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_urno','hora_creacion','estado', 'usuario')}
        ),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Turno, TurnoAdmin)
# Register your models here.
