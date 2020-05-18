from django.urls import path , include
from  . import views


urlpatterns = [
    
    path('RegistroSolicitud', views.ingreso_solicitud , name='registroSolicitud'),
]

