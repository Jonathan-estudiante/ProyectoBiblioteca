from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BookModel(models.Model):

    TIPO = (
        ('t', 'Todos'),
        ('n', 'Novelas'),
        ('cu', 'Cuentos'),
        ('cf', 'Ciencia Ficción'),
        ('r', 'Romance'),
        ('co', 'Comedia'),
        ('p', 'Paranormal'),
        ('f', 'Fantasía'),
        ('ot', 'Otros'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos/')
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=15, choices=TIPO)
    descripcion = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='documentos/')

class HistoryModel(models.Model):

    TIPO = (
        ('n', 'Novelas'),
        ('cu', 'Cuentos'),
        ('cf', 'Ciencia Ficción'),
        ('r', 'Romance'),
        ('co', 'Comedia'),
        ('p', 'Paranormal'),
        ('f', 'Fantasía'),
        ('ot', 'Otros'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos_historias/')
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=15, choices=TIPO, default='ot')
    descripcion = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    text = models.TextField(max_length=6000)