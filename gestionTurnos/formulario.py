from django import forms
from .models import Turno

class CambiarTurnoForm(forms.Form):
    idTurnos=[]
    for id in Turno.objects.all().only('numero_urno'):
        
        idTurnos.append((id.numero_urno, id.numero_urno))
    turno = forms.ChoiceField(choices=idTurnos, label='id turno')
    estados= [('Pendiente', 'Pendiente'), ('Activo', 'Activo'), ('Finalizado', 'Finalizado')]
    estado= forms.ChoiceField(choices=estados, label="Estado del Turno")