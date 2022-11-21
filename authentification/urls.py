from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import URegistration, UserLoginView
urlpatterns = [
    path('login', UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registration', URegistration.as_view(), name='registration'),
]