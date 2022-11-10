from django.db import models
from django.contrib.auth.models import User


class ExtensionUsuario(models.Model):
    # descripcion
    # email
    # avatar = models.ImageField(upload_to='avatares', height_field=50, width_field=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    
      
    
