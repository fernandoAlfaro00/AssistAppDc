from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator , MaxValueValidator

# Create your models here.
class Perfil(models.Model):

    username = models.ForeignKey(User,on_delete=models.CASCADE)
    rut_usuario=models.CharField(unique=True,max_length=15)
    telefono  =  models.PositiveIntegerField(default=0, validators=[MaxValueValidator(900**3)])
    fecha_nacimiento = models.DateField(null=False , blank=False  , default='2001-10-01')