from django.urls import path
from .views import TurnList, VerifUser
urlpatterns = [
    path('turns/', TurnList.as_view(), name='turnList'),
    path('users/<str:identifier>', VerifUser.as_view(), name='verifUser'),
]