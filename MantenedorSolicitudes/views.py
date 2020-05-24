from django.shortcuts import render
from .models import Solicitud 
from .forms import FormularioSolicitud



def ingreso_solicitud(request):
    datos  = {'form': FormularioSolicitud()}
    
    if request.method == 'POST' :

        solicitud_form  =  FormularioSolicitud(request.POST)

        if  solicitud_form.is_valid():
            
            solicitud = solicitud_form.save(commit=False)
            
            #solicitud.codigo = solicitud.general_codigo(solicitud.id_sala.id,solicitud.fecha,solicitud.hora_inicio,solicitud.hora_termino)
            
            if comparar_fecha_hora(solicitud):
                print("no se puede solicitar esta sala a esa hora ya que en uso")
            else:    
                solicitud.save()
        
    

    return render(request , 'app/registro_solicitud.html', datos)


def comparar_fecha_hora(horario):
    
    if Solicitud.objects.filter(id_sala=horario.id_sala,fecha=horario.fecha,hora_inicio__range=(horario.hora_inicio, horario.hora_termino),hora_termino__range=(horario.hora_inicio, horario.hora_termino)).exists():

        return True 
    

def estado_solicitud(request):
    solicitudes =  Solicitud.objects.all()

    datos = {'solicitudes':solicitudes}

    return render(request,'app/listado_solicitudes.html',datos)
