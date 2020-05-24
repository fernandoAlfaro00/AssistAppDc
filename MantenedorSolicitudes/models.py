from django.db import models
from django.core.exceptions import ValidationError
from MantenedorSalas.models import Sala , Horario
from django.contrib.auth.models import User


class   Solicitud(models.Model):
    
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200 , null=False, blank=False)
    horario  = models.OneToOneField(Horario, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    estado_solicitud  = models.BooleanField(default=False)
    codigo  = models.CharField(max_length=15)
    respuesta = models.TextField(max_length=250,null=True,blank=True)
    
   


 
    
