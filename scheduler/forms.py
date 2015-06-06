from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, TextInput
from scheduler.models import Calificacion
from django.forms.models import BaseModelFormSet, modelformset_factory

class CalificacionForm(ModelForm):
    class Meta:
        model = Calificacion
        fields=['evento', 'encuesta', 'puntaje_sesion', 'puntaje_faci']
        widgets = {
            'encuesta': HiddenInput,
            'evento': TextInput(attrs={'readonly':'readonly'})
        }

class BaseCalificacionFormSet(BaseModelFormSet):
    def add_fields(self, form, index):
        super(BaseCalificacionFormSet, self).add_fields(form, index)
        form.fields["Comentarios"] = forms.CharField()

def CalificationFormSet(extra):
    return modelformset_factory(Calificacion, form=CalificacionForm, formset=BaseCalificacionFormSet, extra=extra)
    
