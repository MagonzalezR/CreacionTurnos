from django.shortcuts import render
from gestionTurnos.models import User, Turno
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import TurnoSerializer, UserSerializer

class TurnoList(ModelViewSet):
    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()
    
  
