from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView , CreateView
from .models import Solicitud
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from MantenedorSalas.models import Horario, Sala
from MantenedorUsuarios.models import User
from .forms import FormularioSolicitud, FormularioRepuesta


def ingreso_solicitud(request, id_sala, id_horario):
    
    sala = get_object_or_404(Sala, id=id_sala)
    
    horario = get_object_or_404(Horario, id=id_horario)
    
    datos = {'form': FormularioSolicitud(), 'sala': sala, 'horario': horario}
    

    if request.method == 'POST':

        solicitud_form = FormularioSolicitud(request.POST)


        if solicitud_form.is_valid():
            solicitud = solicitud_form.save(commit=False)
            solicitud.save()

    return render(request, 'app/registro_solicitud.html', datos)


def estado_solicitud(request):
    pass


def respuesta_Solicitud(request, id):

    solicitud = Solicitud.objects.get(id=id)
    form = FormularioRepuesta(instance=solicitud)

    if request.method == 'POST':

        form = FormularioRepuesta(request.POST, instance=solicitud)

        if form.is_valid():

            solicitud = form.save(commit=False)
            solicitud.estado_solicitud = True
            solicitud.save()

            form = FormularioRepuesta(instance=solicitud)

    return render(request, 'app/respuesta_solicitud.html', {'form': form})


def listado_solicitudes(request):
    solicitudes = Solicitud.objects.all()

    datos = {'solicitudes': solicitudes}

    return render(request, 'app/listado_solicitudes.html', datos)


def listado_notificaciones(request):

    return render(request, 'app/listado_notificaciones.html', {})



def ver_notificacion(request):

    pass

class ResponderView(UpdateView):
    
    model =  Solicitud
    form_class  = FormularioRepuesta
    template_name = 'app/respuesta_solicitud.html'
    success_url = reverse_lazy('listadoSolicitudes')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        return context

class SolicitudView(CreateView):

    model = Solicitud
    form_class =  FormularioSolicitud
    template_name ='app/ingreso_solicitud.html'
    success_url = reverse_lazy('listadoSalas')
