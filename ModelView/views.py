from django.shortcuts import render, redirect
from .models import User, Turn
from .formsModel import ChangeTurnForm
from django.contrib.auth.decorators import login_required

@login_required
def changeTurnState(request):
    if not request.user.staff:
        return redirect('home')
    if request.method == "POST":
        
        form =ChangeTurnForm(data=request.POST)
        
        if form.is_valid():
            numTurn = form.cleaned_data['turn']
            stTurn =form.cleaned_data['state']
            newTurno= Turn.objects.get(idTurn=numTurn)
            newTurno.state= stTurn
            newTurno.save()
            return redirect('listTurns')
    else:
        form =ChangeTurnForm()
        return render(request, 'turnState.html',{'form':form})

@login_required
def listTurns(request):
    pending=Turn.objects.filter(state='Pendiente').order_by('-creation')[:5]
    return render(request, 'listTurns.html', {'states':pending})

@login_required
def patients(request):
    patients= User.objects.filter(staff=False, active=True)
    return render(request, 'patients.html', {'patients': patients})

@login_required
def home(request):
    return render(request, 'home.html')
# Create your views here.
