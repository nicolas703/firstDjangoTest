from ast import Try
from tabnanny import check
from venv import create
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from core.models import Usuarios


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        usuario = User.objects.get(username=username)
    except Usuarios.DoesNotExist:
        return Response("Usuario inválido")

    pass_valido = check_password(password, usuario.password)
    if not pass_valido: 
        return Response("Contraseña inválida")
    
    token, created = Token.objects.get_or_create(user=usuario)
    print(token)
    
    return Response(token.key)
