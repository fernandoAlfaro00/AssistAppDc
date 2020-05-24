from django.urls import path , include
from  . import views


urlpatterns = [
    
    path('RegistroSolicitud', views.ingreso_solicitud , name='registroSolicitud'),
    path('ListadoSolicitudes', views.listado_solicitudes , name='listadoSolicitudes'),
    path('RespuestaSolicitud/<int:id>', views.respuesta_Solicitud , name='respuestaSolicitud'),
]

