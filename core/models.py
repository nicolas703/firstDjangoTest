from django.db import models

# Create your models here.
class Usuarios(models.Model):
    email =models.CharField(max_length=100, verbose_name='Email del usuario PK')
    nombre =models.CharField(max_length=100, verbose_name='Nombre del usuario')
    apellido =models.CharField(max_length=100, verbose_name='Apellido del usuario')
    direccion =models.CharField(max_length=100, verbose_name='Direccion del usuario')
    password =models.CharField(max_length=100, verbose_name='Clave del usuario')
    telefono =models.IntegerField(verbose_name='Telefono')

    def __str__(self):
        return self.email
