from django.shortcuts import render
from .models import User, Turno

def cambEstTurno(response):
    return render(response, 'estTurno.html')

def listarEstados(response):
    pendientes=Turno.objects.filter(estado='Pendiente').order_by('-hora_creacion')[:5]
    return render(response, 'listarEstados.html', {'estados':pendientes})

def verPacientes(response):
    pacientes= User.objects.filter(staff=False, active=True)
    return render(response, 'verPacientes.html', {'pacientes': pacientes})

def home(response):
    return render(response, 'Home.html')
# Create your views here.
