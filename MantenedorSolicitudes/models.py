from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Solicitud(models.Model):

    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    horario_inicio = models.DateTimeField()
    horario_final = models.DateTimeField()
    estado_solicitud  = models.BooleanField(default=True)
