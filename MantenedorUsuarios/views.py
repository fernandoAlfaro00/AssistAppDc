from django.shortcuts import render
from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from .models import Perfil
from .forms import  FormularioUsuario , FormularioPerfil

def registro_usuario(request):
    datos = {'perfil_form': FormularioPerfil(),'usuario_form':FormularioUsuario()}

    if request.method == 'POST':

        usuario_form =  FormularioUsuario(request.POST)
        perfil_form  = FormularioPerfil(request.POST)

        if usuario_form.is_valid() & perfil_form.is_valid():
            
            
            #usuario = usuario_form.save()
            perfil  = perfil_form.save(commit=False)
            
            perfil.username =  usuario_form.save()
            
            
            usuario_form.save()

            perfil.save()

            
            datos['perfil_form'] =  perfil_form
            datos['usuario_form'] = usuario_form

            

        

    return render(request,'app/registro_usuario.html',datos)
