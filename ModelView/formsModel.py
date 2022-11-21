from django import forms
from .models import Turn

class ChangeTurnForm(forms.Form):
    idTurns=[]
    for id in Turn.objects.all().only('idTurn'):
        
        idTurns.append((id.idTurn, id.idTurn))
    turn = forms.ChoiceField(choices=idTurns, label='id turno')
    states= [('Pendiente', 'Pendiente'), ('Activo', 'Activo'), ('Finalizado', 'Finalizado')]
    state= forms.ChoiceField(choices=states, label="Estado del Turno")