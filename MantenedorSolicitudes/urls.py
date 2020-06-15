from django.urls import path , include
from  . import views


urlpatterns = [
    
    path('registro/<int:id_sala>/<int:id_horario>', views.ingreso_solicitud , name='registroSolicitud'),
    path('ListadoSolicitudes', views.listado_solicitudes , name='listadoSolicitudes'),
    path('RespuestaSolicitud/<int:pk>', views.ResponderView.as_view() , name='respuestaSolicitud'),
    path('ListadoNotificaciones', views.listado_notificaciones , name='listadoNotificaciones'),
    path('Notificacion', views.ver_notificacion,name ="notificacion"),    

]

