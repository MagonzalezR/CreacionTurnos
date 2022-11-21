from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Turn
from .formsUser import AdminFormUpdateUser, AdminFormCreateUser

    

class CustomUserAdmin(UserAdmin):
    form = AdminFormUpdateUser
    add_form = AdminFormCreateUser

    list_display = ('identifier','name', 'cellphone', 'staff',)
    list_filter = ('identifier','name', 'cellphone', 'staff',)
    fieldsets = (
        (None, {'fields': ('identifier', 'password','name','lastName', 'cellphone', 'picture')}),
        ('Permissions', {'fields': ('staff', 'active', 'admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identifier','name','lastName', 'cellphone', 'picture', 'password1', 'password2', 'staff', 'active', 'admin')}
        ),
    )
    search_fields = ('identifier',)
    ordering = ('identifier',)
    filter_horizontal= ()

class TurnAdmin(admin.ModelAdmin):
    model=Turn
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('idTurn','state', 'user')}
        ),
    )
    def save_model(self, request, obj, form, change):
        obj.userStaff = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Turn, TurnAdmin)
# Register your models here.
