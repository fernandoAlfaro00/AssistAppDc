from django import forms
from .models import  Solicitud

class FormularioSolicitud(forms.ModelForm):

   
    class Meta:
        model =Solicitud
        fields  = ['id_usuario', 'id_sala','descripcion', 'hora_inicio', 'hora_termino' ,'fecha']
        widgets = {
            'fecha' : forms.DateInput(attrs={'type':'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type':'time'}) ,
            'hora_termino' : forms.TimeInput(attrs={'type':'time'}) ,
        }