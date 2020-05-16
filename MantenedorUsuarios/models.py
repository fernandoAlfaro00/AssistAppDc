from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    rut_usuario=models.CharField(unique=True,max_length=20)
    nombre_usuario=models.TextField()
    tipo_usuario=models.CharField(max_length=40)
    correo_ususario=models.EmailField()
    def __str__(self):
      return self.nombre_usuario