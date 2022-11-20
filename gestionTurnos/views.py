from django.shortcuts import render, redirect
from .models import User, Turno
from .formulario import CambiarTurnoForm
from django.contrib.auth.decorators import login_required

@login_required
def cambEstTurno(request):
    if not request.user.staff:
        return redirect('home')
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

@login_required
def listarEstados(request):
    pendientes=Turno.objects.filter(estado='Pendiente').order_by('-hora_creacion')[:5]
    return render(request, 'listarEstados.html', {'estados':pendientes})

@login_required
def verPacientes(request):
    pacientes= User.objects.filter(staff=False, active=True)
    return render(request, 'verPacientes.html', {'pacientes': pacientes})

@login_required
def home(request):
    return render(request, 'Home.html')
# Create your views here.
