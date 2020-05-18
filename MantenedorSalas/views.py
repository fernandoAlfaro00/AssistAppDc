from django.shortcuts import render
from .models import Sala , Horario

def listado_salas(request):

    # pylint: disable=maybe-no-member
    salas  = Sala.objects.all()
    horarios = Horario.objects.all()
    datos = {'salas':salas , 'horarios':horarios}

    return render(request, 'app/listviewSalas.html', datos)
    

