from django.urls import path
from .views import TurnoList, VerifUser
urlpatterns = [
    path('turnos/', TurnoList.as_view(), name='listaTurnos'),
    path('usuarios/<str:cedula>', VerifUser.as_view(), name='verifUser'),
]