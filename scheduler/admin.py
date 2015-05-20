from django.contrib import admin

from .models import Evento, Rol, Salon, Persona, Habitacion
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class PersonaInline(admin.StackedInline):
    model = Persona
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines=[PersonaInline]

class EventoAdmin(admin.ModelAdmin):
    filter_horizontal = ['ocsEncargados', 'asistentes']
    list_display = ['nombre', 'tipo', 'horaInicio', 'horaFin', 'faci']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Rol)
admin.site.register(Salon)
admin.site.register(Persona)
admin.site.register(Habitacion)
# Register your models here.

    
    

