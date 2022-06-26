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
    if request.method == 'POST':
        try:
            formulario = CrearUsuarioForm(data=request.POST, instance=usuario)
            if formulario.is_valid:
                formulario.save()
                datosUsuario['form'] = formulario
                datosUsuario['mensaje'] = "Modificados correctamente"
        except:
            datosUsuario['mensaje'] = "Error, Los campos email, nombre, apellido, direccion y contraseña deben tener menos de 100 dígitos cada uno y el telefono menos de 16 dígitos"
            return render(request, 'core/home.html', datosUsuario)

    return render(request, 'core/home.html', datosUsuario)


def registro(request):
    form = CrearUsuarioForm()
    context = {'form': form}
    context['mensaje'] = ""

    if request.method == 'POST':
        try:
            formulario = CrearUsuarioForm(request.POST)
            if formulario.is_valid:
                usuarioEnDb = Usuarios.objects.filter(
                    email=formulario.data['email']).exists()
                if usuarioEnDb == False:
                    formulario.save()
                    context['mensaje'] = "Guardados correctamente"
                    return redirect("/")
                else:
                    context['mensaje'] = "Error"
                    return render(request, 'core/registro.html', context)
            else:
                context['mensaje'] = "Error"
                return render(request, 'core/registro.html', context)
        except:
            context['mensaje'] = "Error, Los campos email, nombre, apellido, direccion y contraseña deben tener menos de 100 dígitos cada uno y el telefono menos de 16 dígitos"
            return render(request, 'core/registro.html', context)

    return render(request, 'core/registro.html', context)



def login(request):
    context = {'mensaje': ""}

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            usuario = Usuarios.objects.get(email=email)

        except:
            print("Usuario no existe")
            context['mensaje'] = "Error"
            return render(request, 'core/login.html', context)

        if usuario.email == email and usuario.password == password:
            context = {"id": email}
            context['mensaje'] = ""
            return redirect("home/"+email)
        else:
            context['mensaje'] = "Error"
            return render(request, 'core/login.html', context)

    
    return render(request, 'core/login.html', context)


def eliminarUsuario(request, email):

    usuario = Usuarios.objects.get(email=email)
    usuario.delete()

    return redirect("/")
