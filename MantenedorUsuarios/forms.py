from django import forms
from .models import  User ,Perfil

class FormularioUsuario(forms.ModelForm):

    class Meta:

        model=User

        fields = ['username', 'password' , 'first_name', 'last_name', 'email' ]
        



class FormularioPerfil(forms.ModelForm):

    class Meta:

        model=Perfil

        fields = ['rut_usuario', 'fecha_nacimiento', 'telefono']