from django.shortcuts import render, redirect
from .models import User, Turno
from .formulario import CambiarTurnoForm

def cambEstTurno(request):
    if request.method == "POST":
        
        form =CambiarTurnoForm(data=request.POST)
        
        if form.is_valid():
            numTurn = form.cleaned_data['turno']
            estTurn =form.cleaned_data['estado']
            nuevoTurno= Turno.objects.get(numero_urno=numTurn)
            nuevoTurno.estado= estTurn
            nuevoTurno.save()
            return redirect('listarEstados')
    else:
        form =CambiarTurnoForm()
        return render(request, 'estTurno.html',{'form':form})

def listarEstados(request):
    pendientes=Turno.objects.filter(estado='Pendiente').order_by('-hora_creacion')[:5]
    return render(request, 'listarEstados.html', {'estados':pendientes})

def verPacientes(request):
    pacientes= User.objects.filter(staff=False, active=True)
    return render(request, 'verPacientes.html', {'pacientes': pacientes})

def home(request):
    return render(request, 'Home.html')
# Create your views here.
