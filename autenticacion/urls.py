from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import URegistro, UserLoginView
urlpatterns = [
    path('login', UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro', URegistro.as_view(), name='registro'),
]