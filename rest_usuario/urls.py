from django.urls import URLPattern, path
from rest_usuario.views import detalle_usuario, lista_usuarios
from rest_usuario.viewslogin import login 

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name='lista_usuarios'),
    path('detalle_usuario/<id>', detalle_usuario, name='detalle_usuario'),
    path('login', login, name='login'),
]
