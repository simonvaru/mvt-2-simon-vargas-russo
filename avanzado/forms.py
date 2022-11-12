from django import forms
from django import forms


    
class Vehiculo(forms.Form):
    matricula = forms.CharField(max_length=20)
    propietario = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    marca  = forms.CharField(max_length=20)
    cant_puertas = forms.IntegerField()
    color = forms.CharField(max_length=20)
    chasis = forms.CharField(max_length=20)
    avatar = forms.ImageField(required=False)
    
class BusquedaVehiculo(forms.Form):
    matricula = forms.CharField(max_length=20, required=False)        
    
  