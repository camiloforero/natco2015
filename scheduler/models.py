# -*- coding: utf-8 -*-
from colorful.fields import RGBColorField
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
import os
import qrcode
import StringIO

class Bus(models.Model):
    numero = models.PositiveSmallIntegerField(primary_key=True)
    placa = models.CharField(max_length=8, blank=True, null=True)
    capacidad = models.PositiveSmallIntegerField(default=20)
    def __unicode__(self):
        return str(self.numero)
    class Meta:
        verbose_name_plural = "buses"
    
class Salon(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "salones"

class Habitacion(models.Model):
    numero = models.CharField(max_length=16)
    torre = models.CharField(max_length=32)
    capacidad = models.PositiveSmallIntegerField(default=4)
    def __unicode__(self):
        return "%s - %s" % (self.torre, self.numero) 
    class Meta:
        unique_together = (("numero", "torre"))
        ordering = ['torre', 'numero']
        verbose_name_plural = "habitaciones"

class Rol(models.Model):
    tipo = models.CharField(max_length=32, unique=True)
    esConference = models.BooleanField(default=False)
    esLCP = models.BooleanField(default=False)
    def __unicode__(self):
        return self.tipo
    class Meta:
        verbose_name_plural = "roles"

class LC(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    puntos = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = "LC"

class Persona(models.Model):
    user = models.OneToOneField(User, unique=True)
    nombre = models.CharField(max_length=128, default="Sin nombre")
    cedula = models.CharField(max_length=16, blank=True, null=True)
    cargo = models.CharField(max_length=64)
    celular = models.BigIntegerField(blank=True, null=True)
    area = models.CharField(max_length=16)
    rol = models.ForeignKey(Rol, null=True, related_name="personas", on_delete=models.SET_NULL)
    lc = models.ForeignKey(LC, blank=True, null=True, related_name="miembros")
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    esPrivado = models.BooleanField(default=False)
    restricciones = models.CharField(max_length=16, default="No")
    habitacion = models.ForeignKey(Habitacion, related_name="ocupantes", null=True, blank=True, on_delete=models.SET_NULL)
    estaRegistrado = models.BooleanField(default=False, verbose_name="¿Hizo check in?", help_text="Determina si el delegado hizo check in. En caso afirmativo, dicho delegado tendrá acceso completo a la aplicación")
    estaRegistradoVPM = models.BooleanField(default=False, verbose_name="¿Está registrado para VPM?", help_text="Este campo dice si el delegado, asumiendo que asiste a VPM, ya hico check in o no. Aún no tienen acceso completo a la aplicación")
    estaRegistradoVPM2 = models.BooleanField(default=False)
    numMaletas = models.PositiveSmallIntegerField(null=True, blank=True, help_text="La cantidad de maletas que trae esta persona, para hacerle buen tracking", verbose_name="Número de maletas")
    esJD = models.BooleanField(default=False, verbose_name="¿Es jefe de delegación?", help_text="Determina si el delegado es jefe de delegación, lo cual le da algunos permisos extra dentro de la aplicación")
    bus=models.ForeignKey(Bus, related_name="ocupantes", null=True, blank=True)
    puntos = models.PositiveIntegerField(default=0)
    qrRegistro = models.ImageField(upload_to='QR', editable=True, blank=True, null=True, verbose_name="Código QR")
    delegadoNatco = models.BooleanField(default=True, verbose_name="Va a Natco?")
    delegadoVPM = models.BooleanField(default=False, verbose_name="Va a VPM?")
    retroalimentacion = models.TextField(null=True, blank=True, verbose_name="Retroalimentación", help_text="Tu opinión es muy importante para nosotros. Si tienes alguna duda, comentario o feedback, escríbelo en este campo.")
    def __unicode__(self):
        return self.nombre 
    def save(self):
        if not self.qrRegistro:
            if not self.pk:
                super(Persona, self).save()
            username = os.geteuid()
            ausername = os.getegid()
            img = qrcode.make('http://104.131.144.106'+reverse('scheduler:registrar', args=(self.pk,)))
            img_io = StringIO.StringIO()
            img.save(img_io, "JPEG")
            img_file = InMemoryUploadedFile(img_io, None, 'qr1.jpg', 'image/jpg', img_io.len, None)
            self.qrRegistro.save('QR-'+str(self.pk)+'.jpg', img_file, save=False)
        super(Persona, self).save()
    class Meta:
        verbose_name_plural = "personas"

class TipoEvento(models.Model):
    tipo = models.CharField(max_length=32)
    color = RGBColorField(blank=True, null=True)
    colorTexto = RGBColorField(blank=True, null=True, verbose_name="Color del texto")
    esInscribible = models.BooleanField(default=False, help_text="Esto determina si a este evento van todos los asistentes, o es posible inscribirse a el de manera voluntaria")
    esCalificable = models.BooleanField(default=True, help_text="Determina si este evento debería ser calificado por el formulario de feedback de los JDDs")
    def __unicode__(self):
        return self.tipo
    class Meta:
        verbose_name = "Tipo de evento"
        verbose_name_plural = "Tipos de evento"

class Evento(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.ForeignKey(TipoEvento, related_name="eventos", blank=True, null=True, help_text='Qué tipo de evento es? (comidas, plenaria, "Breaking Paradigms", etc.')
    asistentes = models.ManyToManyField(Rol, related_name="eventos", help_text="Acá puedes elegir los grupos de personas que van a asistir a la sesión.", blank=True)
    pAsistentes = models.ManyToManyField(Persona, related_name="eventos", blank=True, verbose_name="Asistentes individuales", help_text="Acá se pueden elegir personas individualmente. Este espacio está pensado para aquellas sesiones que son de elección libre, donde los delegados elegirán su sesión preferida a través de la aplicación. Este campo no debería ser modificado desde acá, al menos que un delegado tenga problemas inscribiéndose")
    horaInicio = models.DateTimeField(default=(datetime(2015, 7, 8, 8, 0, tzinfo=timezone.get_default_timezone() )), verbose_name="Hora de inicio")
    horaFin = models.DateTimeField(default=(datetime(2015, 7, 8, 10, 0, tzinfo=timezone.get_default_timezone() )), verbose_name="Hora fin")
    salon = models.ForeignKey(Salon, related_name="sesiones")
    descripcion = models.TextField(help_text="Esta descripción está disponible para todos los asistentes. Se puede utilizar para darles más información acerca de cualquier parte de la agenda")
    adjuntos = models.FileField(null=True, blank=True)
    facis = models.ManyToManyField(Persona, related_name="sesiones", limit_choices_to=(Q(rol__tipo="MC")|Q(rol__tipo="Chair")), blank=True)
    ocsEncargados = models.ManyToManyField(Persona, related_name="eventosACargo", limit_choices_to={'rol__tipo':'OC'}, blank=True, verbose_name="OCs Encargados")
    descripcionOC = models.TextField(help_text="Esta descripción es visible únicamente por el Conference Team. Utiliza este espacio para colocar información que sea necesaria para que los FACIs y los OCs encargados puedan desarrollar bien sus labores", verbose_name="Descripción Conference Team")
    capacidad=models.PositiveSmallIntegerField(default=400)
    esOpcional = models.BooleanField(default=False, help_text="Dice si el evento es opcional o no. En caso afirmativo, este no aparecerá inicialmente en la agenda de los delegados, y estod deberán inscribirse manualmente a el")
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "eventos"

class Encuesta(models.Model):
    fecha = models.DateField()
    validators = [MinValueValidator(0), MaxValueValidator(5)]
    calOC = models.PositiveSmallIntegerField(validators=validators, verbose_name="Calificación del OC")
    calLgt = models.PositiveSmallIntegerField(validators=validators, verbose_name="Calificación de la logística")
    comentarios = models.TextField()
    lc = models.ForeignKey(LC, related_name='encuestas')
    class Meta:
        unique_together=('fecha', 'lc') 
    def __unicode__(self):
        return "Calificacion de " + self.lc + " el " + self.fecha 
    class Meta:
        verbose_name_plural = "encuestas"

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
    class Meta:
        verbose_name_plural = "calificaciones"


# Create your models here.
