from django import forms
from django.forms import ModelForm
from core.models import Usuarios


class CrearUsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email','nombre','apellido','direccion','password','telefono']
