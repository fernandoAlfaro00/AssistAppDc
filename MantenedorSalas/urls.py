from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('guardar-token/',  views.guardar_token, name='guardar-token'), 
    path('listadoSalas', views.listado_salas , name='listadoSalas'),
    path('horario', views.ingreso_horario , name='horario'),
]
