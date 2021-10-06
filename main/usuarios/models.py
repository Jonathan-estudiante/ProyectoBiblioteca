from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class Usuario(User):
       class Meta:
        proxy = True

class UsuarioBiblioteca(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name
