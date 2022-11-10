# from socket import TIPC_CONN_TIMEOUT
from django.db import models
from django.contrib.auth.models import User #
# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    tipo  = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo}'
    

class Vehiculo(models.Model):
    matricula = models.CharField(max_length=20)
    propietario = models.CharField(max_length=20)    
    modelo = models.CharField(max_length=20)
    marca  = models.CharField(max_length=20)
    cant_puertas = models.IntegerField()
    color = models.CharField(max_length=20)
    chasis = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)#
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)###problema###
    
    def __str__(self):
        return f'Matricula: {self.matricula} \nPropietario: {self.propietario} \nModelo: {self.modelo} \nMarca: {self.marca} \nAvatar: {self.avatar}'


