from django.shortcuts import render
from .models import Sala , Horario
from .forms import HorarioForm
from MantenedorSolicitudes.models import Solicitud

def listado_salas(request):
    # pylint: disable=maybe-no-member
    horarios = Horario.objects.all()
    # pylint: disable=maybe-no-member
    salas  = Sala.objects.all()
   
    datos = {'salas':salas,'horarios':horarios}

    return render(request, 'app/listviewSalas.html', datos)


        

def ingreso_horario(request):
    
    horario_form = HorarioForm()

    if request.method == 'POST' :

        horario_form  =  HorarioForm(request.POST)
    
        if  horario_form.is_valid():

            horario = horario_form.save(commit=False)
            
            if comparar_fecha_hora(horario):
                print("no se puede solicitar esta sala a esa hora ya que en uso")
            else:    
                horario.save()
        
   


    return render(request,'app/ingreso_horario.html',{'horario':horario_form} ) 


def comparar_fecha_hora(horario):
    
    if Horario.objects.filter(sala=horario.sala,fecha=horario.fecha,hora_inicio__range=(horario.hora_inicio, horario.hora_termino),hora_termino__range=(horario.hora_inicio, horario.hora_termino)).exists():

        return True 