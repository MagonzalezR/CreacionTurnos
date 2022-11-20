from rest_framework.serializers import ModelSerializer
from gestionTurnos.models import User, Turno

class TurnoSerializer(ModelSerializer):
    class Meta:
        model = Turno
        fields= ['numero_urno', 'estado', 'usuario']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'