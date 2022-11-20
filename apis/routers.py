from rest_framework.routers import DefaultRouter
from .views import TurnoList

router_turno= DefaultRouter()

router_turno.register(prefix='post',basename='post', viewset=TurnoList)