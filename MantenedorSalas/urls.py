from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    
    path('listadoSalas', views.listado_salas , name='listadoSalas'),
    path('horario', views.ingreso_horario , name='horario'),
]
