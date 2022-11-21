from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Turno
from .forms import AdminFormUpdateUser, AdminFormCreateUser

    

class CustomUserAdmin(UserAdmin):
    form = AdminFormUpdateUser
    add_form = AdminFormCreateUser

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

class TurnAdmin(admin.ModelAdmin):
    model=Turno
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('numero_urno','estado', 'usuario')}
        ),
    )
    def save_model(self, request, obj, form, change):
        obj.usuario_staff = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Turno, TurnAdmin)
# Register your models here.
