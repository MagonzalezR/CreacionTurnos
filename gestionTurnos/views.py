from django.shortcuts import render

def cambEstTurno(response):
    return render(response, 'estTurno.html')

def listarEstados(response):
    return render(response, 'listarEstados.html')

def verPacientes(response):
    return render(response, 'verPacientes.html')

def home(response):
    return render(response, 'Home.html')
# Create your views here.
