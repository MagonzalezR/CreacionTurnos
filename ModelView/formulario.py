from django import forms
from .models import Turno

class ChangeTurnForm(forms.Form):
    idTurns=[]
    for id in Turno.objects.all().only('numero_urno'):
        
        idTurns.append((id.numero_urno, id.numero_urno))
    turn = forms.ChoiceField(choices=idTurns, label='id turno')
    states= [('Pendiente', 'Pendiente'), ('Activo', 'Activo'), ('Finalizado', 'Finalizado')]
    state= forms.ChoiceField(choices=states, label="Estado del Turno")