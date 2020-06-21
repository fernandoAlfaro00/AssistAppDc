from django.db import models
from django.core.exceptions import ValidationError


class Sala(models.Model):
    nombre_sala = models.CharField(max_length=30)
    piso_sala = models.IntegerField()
    descripcion_sala = models.TextField(max_length=500)
    estado_sala = models.BooleanField()
    sede =   models.CharField(max_length=30,blank=False)
    edificio  =  models.CharField(max_length=30 ,blank=False)
    disponibilidad = models.BooleanField(default=True, blank=True)   

    def __str__(self):
      return self.nombre_sala


class Horario(models.Model):

    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    sala = models.ForeignKey(Sala,on_delete=models.CASCADE,
                            null=False,blank=False,related_name='horarios')
    
    def __str__(self):
      return 'fecha : {}- desde {} y hasta {}'.format(self.fecha,self.hora_inicio, self.hora_termino)
      
    def clean_horario(self):

      if self.hora_inicio >=  self.hora_termino :

        return ValidationError('La hora de termino debe ser mayor a la de inicio')

    
    
    def general_codigo(self,sala,fecha,inicio,termino):
        codigo = ''
        codigo_bruto  = '{}{}{}{}'.format(sala,fecha,inicio,termino) 

        for i in codigo_bruto :

            if i.isdigit():

                codigo = codigo + i 

        return codigo
    


