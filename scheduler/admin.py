# coding:utf-8
from __future__ import unicode_literals
from django.contrib import admin

from django import forms
from django.conf.urls import url
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.admin.sites import AdminSite
from django.db.models import Q
from django.utils.html import format_html

from .models import Evento, Rol, Salon, Persona, Habitacion, LC, Bus, TipoEvento
from . import admin_views

class EventAdminSite(AdminSite):
    site_header = "Administración de Starway 2016"
    site_title = "Starway 2016"
    index_title = "Administración de la aplicación de Starway"
    index_template = "event_admin/index.html"

    def get_urls(self):
        urls = super(EventAdminSite, self).get_urls()
        event_urls = [
            url(r'^subir_delegados/$', self.admin_view(admin_views.UploadDelegatesView.as_view()), name='subir_delegados'),
            url(r'^subir_conference/$', self.admin_view(admin_views.UploadConferenceView.as_view()), name='subir_conference'),
            url(r'^subir_habitaciones/$', self.admin_view(admin_views.UploadRoomsView.as_view()), name='subir_habitaciones'),
            ]
        return urls + event_urls

admin_site = EventAdminSite(name='event_admin')

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields=['numero', 'torre', 'capacidad', 'ocupantes']

    ocupantes = forms.ModelMultipleChoiceField(queryset = None, required=False)
    def __init__(self, *args, **kwargs):
        super(HabitacionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['ocupantes'].initial = self.instance.ocupantes.all()
            self.fields['ocupantes'].queryset = Persona.objects.filter((Q(habitacion=self.instance)|Q(habitacion=None))&Q(delegadoNatco=True)).select_related('user')

    def save(self, *args, **kwargs):
        instance = super(HabitacionForm, self).save()
        self.fields['ocupantes'].initial.update(habitacion=None)
        self.cleaned_data['ocupantes'].update(habitacion=instance)
        return instance
    def save_m2m(self):
        pass

class HabitacionAdmin(admin.ModelAdmin):
    form = HabitacionForm
    list_display = ['__str__', 'capacidad', 'ocupancia']

    def ocupancia(self, obj):
        total = obj.ocupantes.count()
        diff = obj.capacidad - total
        html = '<span style="color: #{};">{}/{}</span>'
        if diff > 0:
            color = "00CC00"
        elif diff == 0:
            color = "CCCC00"
        else:
            color = "FF0000"
        return format_html(html, color, total, obj.capacidad)

class PersonaInline(admin.StackedInline):
    model = Persona
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines=[PersonaInline]
    list_display = ['nombre', 'rol', 'lc', 'bus', 'habitacion']
    list_select_related=('persona__nombre', 'persona__rol', 'persona__lc', 'persona__habitacion')

    def nombre(self, obj):
        return obj.persona.nombre
    nombre.short_description = 'Nombre'

    def rol(self, obj):
        return obj.persona.rol
    rol.short_description = 'Rol'

    def lc(self, obj):
        return obj.persona.lc
    lc.short_description = 'LC'

    def bus(self, obj):
        return obj.persona.bus
    bus.short_description = 'Bus'

    def habitacion(self, obj):
        return obj.persona.habitacion
    rol.short_description = 'Habitacion'

class EventoAdmin(admin.ModelAdmin):
    filter_horizontal = ['ocsEncargados', 'asistentes', 'pAsistentes', 'facis']
    list_display = ['nombre', 'tipo', 'salon', 'horaInicio', 'horaFin',]
    list_select_related = ('salon','tipo')
    fields= ('nombre', 'tipo', 'salon', 'asistentes', ('horaInicio', 'horaFin'), 'facis', 'ocsEncargados', 'descripcion', 'descripcionOC', 'adjuntos', 'pAsistentes')
    save_on_top = True

#class CalificacionAdmin(admin.ModelAdmin):
#    list_display = ['evento', 'lc', 'puntaje_sesion', 'puntaje_faci']

#admin_site.unregister(User)
#admin_site.unregister(Group)
admin_site.register(User, UserAdmin)
admin_site.register(Evento, EventoAdmin)
admin_site.register(Habitacion, HabitacionAdmin)
admin_site.register(Rol)
admin_site.register(Salon)
admin_site.register(LC)
#admin_site.register(Calificacion, CalificacionAdmin)
admin_site.register(Bus)
admin_site.register(TipoEvento)

    
    

