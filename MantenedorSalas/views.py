from django.shortcuts import render
from .models import Sala , Horario
from .forms import HorarioForm
from MantenedorSolicitudes.models import Solicitud
def listado_salas(request):

    # pylint: disable=maybe-no-member
    salas  = Sala.objects.all()
    #horarios = Horario.objects.all()
    datos = {'salas':salas }

    return render(request, 'app/listviewSalas.html', datos)


        

def ingreso_horario(request):
    
    horario_form = HorarioForm()

    if request.method == 'POST' :

        horario_form  =  HorarioForm(request.POST)
    
        # if  horario_form.is_valid():

        #     horario = horario_form.save(commit=False)
            
        #     horario.save()
   


    return render(request,'app/ingreso_horario.html',{'horario':horario_form} ) 


