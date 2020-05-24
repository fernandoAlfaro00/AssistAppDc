from django.db import models
from django.core.exceptions import ValidationError
from MantenedorSalas.models import Sala
from django.contrib.auth.models import User


class   Solicitud(models.Model):
    
    
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200 , null=False, blank=False)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    estado_solicitud  = models.BooleanField(default=True)
    codigo  = models.CharField(max_length=15)
    
    def clean_horario(self):
       
        if self.hora_termino <= self.hora_inicio:
             raise ValidationError('La horario de termino debe ser mayor a la de inicio')

    
    def general_codigo(self,sala,fecha,inicio,termino):
        codigo = ''
        codigo_bruto  = '{}{}{}{}'.format(sala,fecha,inicio,termino) 

        for i in codigo_bruto :

            if i.isdigit():

                codigo = codigo + i 

        return codigo
    


 
    
