from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class TipodeTramite(models.Model):

    Tramite = models.CharField(max_length=40)
    Fechainicio = models.DateField()

class Documentacion(models.Model):

    documento = models.CharField(max_length=40)

class Pago(models.Model):

    metododepago = models.CharField(max_length=40)
    pagado = models.BooleanField()