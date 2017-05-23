from django.db import models
from django.contrib.auth.models import User , Group

# Create your models here.

class Comprador(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    favoritos = models.ManyToManyField(Vendedor)


class Vendedor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    foto = models.CharField(max_length=100)


class VendedorAmbulante(models.Model):
    user = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    activo = models.BooleanField(default=False)

class VendedorFijo(models.Model):
    user = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    horaInicio = models.IntegerField()
    minutoInicio = models.IntegerField()
    horaFin = models.IntegerField()
    minutoFin = models.IntegerField()

class Producto(models.Model):
    vendedor = models.ForeignKey(
        'Vendedor',
        on_delete=models.CASCADE,
    )
    foto = models.CharField(max_length=100)
    descripcion= models.CharField(max_length=500)
    stock = models.IntegerField()
    precio = models.IntegerField()
    categorias = models.ManyToManyField(Categorias)


class Categorias(models.Model):
	tipo =models.CharField(max_length=25)










