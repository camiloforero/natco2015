from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, TextInput, MultipleHiddenInput
from scheduler.models import Calificacion, Encuesta, Evento, Persona
from django.forms.models import BaseModelFormSet, modelformset_factory

class EventoFileForm(ModelForm):
    class Meta:
        model = Evento
        fields=['adjuntos']

class FeedbackForm(ModelForm):
    class Meta:
        model = Persona
        fields=['retroalimentacion']

class EventoDescripcionForm(ModelForm):
    class Meta:
        model = Evento
        fields=['descripcionOC']

class CalificacionForm(ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        evt = cleaned_data.get('evento')
        print "nombre: "+evt
        evento = Evento.objects.get(nombre=evt)
        print evento
        cleaned_data['evento'] = evento
        return cleaned_data
    class Meta:
        model = Calificacion
        fields=['evento', 'puntaje_sesion', 'puntaje_faci']
        widgets = {
            'evento': HiddenInput()
        }
class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = ['fecha', 'calOC', 'calLgt', 'comentarios']
        widgets = { 
            'fecha':HiddenInput()
        }


def CalificationFormSet(extra):
    return modelformset_factory(Calificacion, form=CalificacionForm, extra=extra)
    
