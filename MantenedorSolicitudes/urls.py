from django.urls import path , include
from  . import views


urlpatterns = [
    
    path('registro/<int:id_sala>/<int:id_horario>', views.ingreso_solicitud , name='registroSolicitud'),
    path('ListadoSolicitudes', views.listado_solicitudes , name='listadoSolicitudes'),
    path('RespuestaSolicitud/<int:id>', views.respuesta_Solicitud , name='respuestaSolicitud'),

]
