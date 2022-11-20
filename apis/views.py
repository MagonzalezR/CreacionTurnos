from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from gestionTurnos.models import User, Turno

class TurnoList(View):
    def get(self, request):
        turnos= list(Turno.objects.values())
        if(len(turnos)>0):
            datos={'message':'succes', 'turnos': turnos}
        else:
            datos={'message':'No turns aviable'}
        return JsonResponse(datos)    
  
class VerifUser(View):
    def get(self, request, cedula=""):
        if cedula =="":
            datos={'message':'No given id'}
        else:
            usuarios= list(User.objects.filter(cedula=cedula).values())
            if len(usuarios)>0:
                datos={'message':'succes', 'usuarios': usuarios}
            else:
                datos={'message':'User not found'}
        return JsonResponse(datos)