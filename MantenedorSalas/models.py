from django.db import models

# Create your models here.

class Sala(models.Model):
    nombre_sala = models.CharField(max_length=30)
    piso = models.IntegerField()
    descripcion = models.TextField(max_length=500)
    estado = models.BooleanField()

    def __str__(self):
      return self.nombre_sala


class Horario(models.Model):
    fecha = models.DateTimeField()
    hora_inicio = models.DateTimeField()
    hora_termino = models.DateTimeField()

    def __str__(self):
      return self.fecha




