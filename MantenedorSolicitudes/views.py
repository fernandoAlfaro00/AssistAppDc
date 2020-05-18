from django.shortcuts import render
from .models import Solicitud
from .forms import FormularioSolicitud



def ingreso_solicitud(request):
    datos  = {'form': FormularioSolicitud()}
    
    if request == 'POST' :

        solicitud  =  FormularioSolicitud(request.POST)
        
        
        

    return render(request , 'app/registro_solicitud.html', datos)