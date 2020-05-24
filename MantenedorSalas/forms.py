from django import forms
from django.db.models.functions import datetime
from .models import Horario

# forms.DateInput.input_type="date"
# forms.TimeInput.input_type="time"
class HorarioForm(forms.ModelForm):
        

       
        class Meta:
            
            model = Horario
            fields  = [ 'hora_inicio' , 'hora_termino' ,'sala' ]
            widgets = {
           
            'hora_inicio': forms.SplitDateTimeWidget(date_attrs={'type':'date' ,},
                                                    time_attrs={'type':'time' ,}),
            'hora_termino': forms.SplitDateTimeWidget(date_attrs={'type':'date' ,},
                                                    time_attrs={'type':'time' ,})   
                                                    ,
                      

        }
        
        
       
       

        