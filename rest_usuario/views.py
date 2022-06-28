import email
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuarios
from .serializers import UsuarioSerializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_usuarios(request):
    """
    Lista todos los usuarios
    """
    if request.method =='GET':
        usuario = Usuarios.objects.all()
        serializer=UsuarioSerializer(usuario,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_usuario(request,id):
    """ 
        Get,update,odelete de un vehiculo en particular
    """
    try:
        usuario=Usuarios.objects.get(email=id)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer=UsuarioSerializer(usuario)
        return Response(serializer.data)
    if request.method =='PUT':
        data=JSONParser().parse(request)
        serializer=UsuarioSerializer(usuario,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)