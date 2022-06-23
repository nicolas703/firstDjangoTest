import email
import re
from django.shortcuts import redirect, render

from core.forms import CrearUsuarioForm
from .models import Usuarios

# Create your views here.


def home(request, id):
    usuario = Usuarios.objects.get(email=id)

    datosUsuario = {
        'form': CrearUsuarioForm(instance=usuario)
    }
    if request.method =='POST':
        formulario=CrearUsuarioForm(data=request.POST,instance=usuario)
        if formulario.is_valid:
            formulario.save()
            datosUsuario['form'] = formulario
            datosUsuario['mensaje']="Modificados correctamente"

    return render(request, 'core/home.html', datosUsuario)


def registro(request):
    form = CrearUsuarioForm()
    context = {'form': form}
    context['mensaje'] = ""

    if request.method == 'POST':
        formulario = CrearUsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            context['mensaje'] = "Guardados correctamente"

    return render(request, 'core/registro.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            usuario = Usuarios.objects.get(email=email)

        except:
            print("Usuario no existe")

        if usuario.email == email and usuario.password == password:
            context = {"id": email}
            return redirect("home/"+email)

    return render(request, 'core/login.html')


def eliminarUsuario(request, email):
    
    usuario = Usuarios.objects.get(email=email)
    usuario.delete()

    return redirect("/")
