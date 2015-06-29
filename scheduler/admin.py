from django.contrib import admin

from .models import Evento, Rol, Salon, Persona, Habitacion, LC, Bus, TipoEvento
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.db.models import Q
from django.utils.html import format_html

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields=['numero', 'capacidad', 'ocupantes']

    ocupantes = forms.ModelMultipleChoiceField(queryset = None, required=False)
    def __init__(self, *args, **kwargs):
        super(HabitacionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['ocupantes'].initial = self.instance.ocupantes.all()
            self.fields['ocupantes'].queryset = Persona.objects.filter(Q(habitacion=self.instance)|Q(habitacion=None)).select_related('user')

    def save(self, *args, **kwargs):
        instance = super(HabitacionForm, self).save()
        self.fields['ocupantes'].initial.update(habitacion=None)
        self.cleaned_data['ocupantes'].update(habitacion=instance)
        return instance
    def save_m2m(self):
        pass

class HabitacionAdmin(admin.ModelAdmin):
    form = HabitacionForm
    list_display = ['numero', 'capacidad', 'ocupancia']

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
    list_display = ['name', 'rol', 'lc', 'bus']
    list_select_related=('persona__rol', 'persona__lc')

    def name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name))
    name.short_description = 'Nombre'

    def lc(self, obj):
        return obj.persona.lc
    lc.short_description = 'LC'

    def bus(self, obj):
        return obj.persona.bus
    bus.short_description = 'Bus'
    def rol(self, obj):
        return obj.persona.rol
    rol.short_description = 'Rol'

class EventoAdmin(admin.ModelAdmin):
    filter_horizontal = ['ocsEncargados', 'asistentes', 'pAsistentes', 'facis']
    list_display = ['nombre', 'tipo', 'salon', 'horaInicio', 'horaFin',]
    list_select_related = ('salon','tipo')
    fields= ('nombre', 'tipo', 'salon', 'asistentes', ('horaInicio', 'horaFin'), 'facis', 'ocsEncargados', 'descripcion', 'descripcionOC', 'adjuntos', 'pAsistentes')
    save_on_top = True

#class CalificacionAdmin(admin.ModelAdmin):
#    list_display = ['evento', 'lc', 'puntaje_sesion', 'puntaje_faci']

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Rol)
admin.site.register(Salon)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(LC)
#admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Bus)
# Register your models here.
admin.site.register(TipoEvento)

    
    

