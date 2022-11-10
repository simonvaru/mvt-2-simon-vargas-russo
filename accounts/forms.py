from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MiFormularioDeCreacion(UserCreationForm):
    
    username = forms.CharField(label='Nombre Usuario', max_length=20)
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model =User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields }

class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    avatar = forms.ImageField(required=False)
     

    
    
    
            