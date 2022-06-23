import imp
from multiprocessing.spawn import import_main_path
from django.urls import URLPattern, path
from .views import registro, eliminarUsuario, login, home

urlpatterns = [
    path('home/<id>', home, name='home'),
    path('', login, name='login'),
    path('registro', registro, name='registro'),
    path('eliminarUsuario/<email>', eliminarUsuario, name='eliminarUsuario'),
]
