from django.shortcuts import render
from .models import Sala , Horario

def listado_salas(request):

    # pylint: disable=maybe-no-member
    salas  = Sala.objects.all()

    datos = {'salas':salas}

    return render(request, 'app/listviewSalas.html', datos)
    
