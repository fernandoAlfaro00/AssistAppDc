from django import forms
from .models import  Solicitud

class FormularioSolicitud(forms.ModelForm):

    class Meta:
        model =Solicitud
        fields  = ['id_usuario', 'descripcion', 'horario_inicio', 'horario_final', 'estado_solicitud']
        