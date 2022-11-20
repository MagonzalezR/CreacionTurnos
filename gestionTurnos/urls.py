from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('estTurno', views.cambEstTurno, name='estTurno'),
    path('listarEstados', views.listarEstados, name='listarEstados'),
    path('verPacientes', views.verPacientes, name='verPacientes'),
    path('', views.home, name='home'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)