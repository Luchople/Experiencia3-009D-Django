from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=25, verbose_name='nombre') 
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    rut = models.CharField(max_length=9, primary_key=True, verbose_name='rut') 

    def __str__(self):
        return self.rut

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6, verbose_name='codigo')
    precio = models.IntegerField(verbose_name='precio')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    nombre = models.CharField(max_length=25, verbose_name='nombre')

    def __str__(self):
        return self.codigo
