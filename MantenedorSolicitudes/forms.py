from django import forms
from .models import  Solicitud

class FormularioSolicitud(forms.ModelForm):


    class Meta:

        model =Solicitud
        fields  = ['usuario', 'sala','descripcion', 'horario']


class FormularioRepuesta(forms.ModelForm):

    
    class Meta:
        
        model= Solicitud
        fields = ['usuario','respuesta', 'estado_solicitud']
        widgets = {
            'respuesta': forms.Textarea(attrs={'class' :'form-control',}),
            'usuario': forms.HiddenInput(),

            

        }    