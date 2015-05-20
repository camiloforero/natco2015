from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.utils import timezone
class Salon(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    def __unicode__(self):
        return self.nombre

class Habitacion(models.Model):
    numero = models.CharField(max_length=16, unique=True)
    def __unicode__(self):
        return self.numero

class Rol(models.Model):
    tipo = models.CharField(max_length=32, unique=True)
    def __unicode__(self):
        return self.tipo

class Persona(models.Model):
    user = models.OneToOneField(User)
    cedula = models.CharField(max_length=16, blank=True, null=True)
    cargo = models.CharField(max_length=32)
    celular = models.BigIntegerField(blank=True, null=True)
    rol = models.ForeignKey(Rol, related_name="personas")
    lc = models.CharField(max_length = 16)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    esPrivado = models.BooleanField(default=True)
    habitacion = models.ForeignKey(Habitacion, related_name="ocupantes", null=True, blank=True)
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name 

class Evento(models.Model):
    asistentes = models.ManyToManyField(Rol, related_name="eventos")
    horaInicio = models.DateTimeField(default=(datetime(2015, 7, 4, 8, 0, tzinfo=timezone.get_default_timezone() )))
    horaFin = models.DateTimeField(default=(datetime(2015, 7, 4, 10, 0, tzinfo=timezone.get_default_timezone() )))
    nombre = models.CharField(max_length=30, unique=True)
    salon = models.ForeignKey(Salon)
    adjuntos = models.FileField(null=True, blank=True)
    faci = models.ForeignKey(Persona, null=True, related_name="sesiones")
    ocsEncargados = models.ManyToManyField(Persona, related_name="eventosACargo")
    TIPO1 = 'Work it harder'
    TIPO2 = 'Make it better'
    TIPO3 = 'Do it faster'
    TIPO4 = 'Make us stronger'
    TIPO_CHOICES = (
        (TIPO1, TIPO1),
        (TIPO2, TIPO2),
        (TIPO3, TIPO3),
        (TIPO4, TIPO4),
    )
    tipo = models.CharField(max_length=32, choices=TIPO_CHOICES, null=True, blank=True)
    def __unicode__(self):
        return self.nombre






# Create your models here.
