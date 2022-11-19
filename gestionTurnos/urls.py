from django.urls import path
from . import views

urlpatterns = [
    path('estTurno', views.cambEstTurno, name='estTurno'),
    path('listarEstados', views.listarEstados, name='listarEstados'),
    path('verPacientes', views.cambEstTurno, name='verPacientes'),
    path('', views.home, name='home'),
]