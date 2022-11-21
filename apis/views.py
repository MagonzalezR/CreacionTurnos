from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from ModelView.models import User, Turn

class TurnList(View):
    def get(self, request):
        turns= list(Turn.objects.values())
        if(len(turns)>0):
            data={'message':'succes', 'turns': turns}
        else:
            data={'message':'No turns aviable'}
        return JsonResponse(data)    
  
class VerifUser(View):
    def get(self, request, identifier=""):
        if identifier =="":
            data={'message':'No given id'}
        else:
            users= list(User.objects.filter(identifier=identifier).values())
            if len(users)>0:
                data={'message':'succes', 'user': users}
            else:
                data={'message':'User not found'}
        return JsonResponse(data)