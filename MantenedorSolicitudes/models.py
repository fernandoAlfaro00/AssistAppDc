from django.db import models
from django.core.exceptions import ValidationError
from MantenedorSalas.models import Sala , Horario
from django.contrib.auth.models import User


class ModeloBase(models.Model):
    
    id = models.AutoField(primary_key = True)
    fecha_creacion = models.DateField(auto_now= False, auto_now_add= True)
    fecha_modificacion = models.DateField(auto_now=True  ,   auto_now_add=False)
    fecha_eliminacion = models.DateField(auto_now=True  ,   auto_now_add=False)
    class Meta :
        abstract = True 

class   Solicitud(ModeloBase):
    
    ESTADO_SOLICITUD_CHOICES =[
        ('a', 'Aceptada'),
        ('r', 'Rechazada'),
        ('e','No Vista'),
    ]    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=150 , null=False, blank=False)
    horario  = models.OneToOneField(Horario, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    estado_solicitud  = models.CharField( max_length=2 , choices=ESTADO_SOLICITUD_CHOICES, default='e' )
    codigo  = models.CharField(max_length=15)

    respuesta = models.TextField(max_length=150,null=True,blank=True)
       


 
    

