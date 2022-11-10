from django import forms
from django import forms

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo  = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    
class Vehiculo(forms.Form):
    matricula = forms.CharField(max_length=20)
    propietario = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    marca  = forms.CharField(max_length=20)
    cant_puertas = forms.IntegerField()
    color = forms.CharField(max_length=20)
    chasis = forms.CharField(max_length=20)
        
    
    