from django import forms
from django.db.models.functions import datetime
from .models import Horario

# forms.DateInput.input_type="date"
# forms.TimeInput.input_type="time"
class HorarioForm(forms.ModelForm):
        

       
        class Meta:
            
            model = Horario
            fields  = [ 'sala','fecha','hora_inicio' , 'hora_termino' ]
            widgets = {
                'fecha' : forms.DateInput(attrs={'type':'date' , 'class': 'form-control'}),
                'hora_inicio': forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}) ,
                'hora_termino' : forms.TimeInput(attrs={'type':'time' , 'class': 'form-control'}) ,
            }
            
        
       
       

        