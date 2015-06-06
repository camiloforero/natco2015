from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
import qrcode
import StringIO

class Bus(models.Model):
    placa = models.CharField(max_length=8, unique=True)
    capacidad = models.PositiveSmallIntegerField(default=20)
    def __unicode__(self):
        return self.placa
    
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
    esConference = models.BooleanField(default=False)
    esJD = models.BooleanField(default=False)
    esLCP = models.BooleanField(default=False)
    def __unicode__(self):
        return self.tipo

class LC(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    puntos = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.nombre

class Persona(models.Model):
    user = models.OneToOneField(User, unique=True)
    cedula = models.CharField(max_length=16, blank=True, null=True)
    cargo = models.CharField(max_length=32)
    celular = models.BigIntegerField(blank=True, null=True)
    area = models.CharField(max_length=16)
    rol = models.ForeignKey(Rol, related_name="personas")
    lc = models.ForeignKey(LC, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    esPrivado = models.BooleanField(default=False)
    habitacion = models.ForeignKey(Habitacion, related_name="ocupantes", null=True, blank=True)
    estaRegistrado = models.BooleanField(default=False)
    bus=models.ForeignKey(Bus, related_name="ocupantes", null=True, blank=True)
    puntos = models.IntegerField(default=0)
    qrRegistro = models.ImageField(upload_to='QR', editable=True)
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name 
    def save(self):
        if not self.pk:
            self = super(Persona, self).save(commit=False)
        img = qrcode.make('http://192.241.211.190:8000'+reverse('scheduler:registrar', args=(self.pk,)))
        img_io = StringIO.StringIO()
        img.save(img_io, "JPEG")
        img_file = InMemoryUploadedFile(img_io, None, 'qr1.jpg', 'image/jpg', img_io.len, None)
        self.qrRegistro.save('QR-'+str(self.pk)+'.jpg', img_file, save=False)
        super(Persona, self).save()

class Evento(models.Model):
    asistentes = models.ManyToManyField(Rol, related_name="eventos")
    pAsistentes = models.ManyToManyField(Persona, related_name="eventos", blank=True)
    horaInicio = models.DateTimeField(default=(datetime(2015, 7, 4, 8, 0, tzinfo=timezone.get_default_timezone() )))
    horaFin = models.DateTimeField(default=(datetime(2015, 7, 4, 10, 0, tzinfo=timezone.get_default_timezone() )))
    nombre = models.CharField(max_length=30, unique=True)
    salon = models.ForeignKey(Salon, related_name="sesiones")
    descripcion = models.TextField()
    capacidad = models.IntegerField(default=400)
    adjuntos = models.FileField(null=True, blank=True)
    facis = models.ManyToManyField(Persona, related_name="sesiones", limit_choices_to={'rol__tipo':'FACI'})
    ocsEncargados = models.ManyToManyField(Persona, related_name="eventosACargo", limit_choices_to={'rol__tipo':'OC'})
    descripcionOC = models.TextField()
    capacidad=models.PositiveSmallIntegerField(default=100)
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

class Encuesta(models.Model):
    fecha = models.DateField()
    validators = [MinValueValidator(0), MaxValueValidator(5)]
    calOC = models.PositiveSmallIntegerField(validators=validators)
    calLgt = models.PositiveSmallIntegerField(validators=validators)
    comentarios = models.TextField()
    lc = models.ForeignKey(LC, related_name='encuestas')
    class Meta:
        unique_together=('fecha', 'lc') 
    def __unicode__(self):
        return "Calificacion de " + self.lc + " el " + self.fecha 

class Calificacion(models.Model):
    evento = models.ForeignKey(Evento, related_name='calificacionLC')
    encuesta = models.ForeignKey(Encuesta, related_name='calificacionEvento')
    validators = [MinValueValidator(0), MaxValueValidator(5)]
    puntaje_sesion = models.PositiveSmallIntegerField(validators = validators)
    puntaje_faci = models.PositiveSmallIntegerField(validators = validators)
    class Meta:
        unique_together = ('evento', 'encuesta')
    def __unicode__(self):
        return "Calificacion: " + self.evento + " - " + self.encuesta.lc


# Create your models here.
