
from django.db import models
from django.contrib.auth.models import User , Group

class Categorias(models.Model):
    tipo = models.CharField(max_length=25)

class Vendedor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    acepta_Efectivo = models.BooleanField()
    acepta_Credito = models.BooleanField()
    acepta_Debito = models.BooleanField()
    acepta_Junaeb = models.BooleanField()
    avatar = models.FileField(blank=True, upload_to='profileImage')


class Comprador(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    favoritos = models.ManyToManyField(Vendedor)
    avatar = models.IntegerField()


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
    nombre = models.CharField(max_length=200,default="Sin nombre")
    foto = models.FileField(blank=True, upload_to='productoImage', default = None)
    fotoPrev = models.CharField(max_length=1000, default="../../static/img/fries.png")
    descripcion= models.CharField(max_length=500)
    stock = models.IntegerField()
    precio = models.IntegerField()
    categorias = models.ManyToManyField(Categorias)










