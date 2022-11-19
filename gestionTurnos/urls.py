from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('estTurno', views.cambEstTurno, name='estTurno'),
    path('listarEstados', views.listarEstados, name='listarEstados'),
    path('verPacientes', views.verPacientes, name='verPacientes'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.home, name='home'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)