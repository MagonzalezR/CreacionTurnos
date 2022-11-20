from django.urls import path, include
from .routers import router_turno
urlpatterns = [
    path('turnos/', include(router_turno.urls), name='listaTurnos'),
]