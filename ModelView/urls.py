from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('turnState', views.changeTurnState, name='turnState'),
    path('listTurns', views.listTurns, name='listTurns'),
    path('patients', views.patients, name='patients'),
    path('', views.home, name='home'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)