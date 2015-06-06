from django.contrib import admin

from .models import Evento, Rol, Salon, Persona, Habitacion, LC, Bus
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class PersonaInline(admin.StackedInline):
    model = Persona
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines=[PersonaInline]
    list_display = ['name', 'rol', 'lc', 'bus']

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
    list_display = ['nombre', 'tipo', 'horaInicio', 'horaFin',]

#class CalificacionAdmin(admin.ModelAdmin):
#    list_display = ['evento', 'lc', 'puntaje_sesion', 'puntaje_faci']

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Rol)
admin.site.register(Salon)
admin.site.register(Habitacion)
admin.site.register(LC)
#admin.site.register(Calificacion, CalificacionAdmin)
admin.site.register(Bus)
# Register your models here.

    
    

