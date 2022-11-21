from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from ModelView.models import User, Turno

class TurnList(View):
    def get(self, request):
        turns= list(Turno.objects.values())
        if(len(turns)>0):
            data={'message':'succes', 'turnos': turns}
        else:
            data={'message':'No turns aviable'}
        return JsonResponse(data)    
  
class VerifUser(View):
    def get(self, request, identifier=""):
        if identifier =="":
            data={'message':'No given id'}
        else:
            users= list(User.objects.filter(cedula=identifier).values())
            if len(users)>0:
                data={'message':'succes', 'usuarios': users}
            else:
                data={'message':'User not found'}
        return JsonResponse(data)