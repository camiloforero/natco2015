#coding:utf-8
from __future__ import unicode_literals

from csv import DictReader

from django.views.generic.edit import FormView
from django.http import HttpResponse

from . import admin_forms, scripts

class UploadDelegatesView(FormView):
    template_name = 'event_admin/admin_single_form.html'
    form_class = admin_forms.UploadDelegatesForm
    success_url = 'whatever' #No es necesaria, ya que el método form_valid retorna la página de una vez

    def form_valid(self, form): #Este método, cuando están validados los campos del csv que se subió (lo cual sucede en el método clean de UploadDelegatesForm), crea a todos los usuarios a partir de los datos que se encuentran en el archivo csv subido.
        csv = self.request.FILES['csv'].file
        reader = DictReader(csv)
        return_message = ""
        for row in reader:
            return_message += scripts.create_delegate(row) + "<br/>"
        return HttpResponse(return_message)

class UploadConferenceView(FormView):
    template_name = 'event_admin/admin_single_form.html'
    form_class = admin_forms.UploadConferenceForm
    success_url = 'whatever' #No es necesaria, ya que el método form_valid retorna la página de una vez
    def form_valid(self, form): #Este método, cuando están validados los campos del csv que se subió (lo cual sucede en el método clean de UploadDelegatesForm), crea a todos los usuarios a partir de los datos que se encuentran en el archivo csv subido.
        csv = self.request.FILES['csv'].file
        reader = DictReader(csv)
        return_message = ""
        for row in reader:
            return_message += scripts.create_conference(row) + "<br/>"
        return HttpResponse(return_message)

class UploadRoomsView(FormView):
    template_name = 'event_admin/admin_single_form.html'
    form_class = admin_forms.UploadRoomsForm
    success_url = 'whatever' #No es necesaria, ya que el método form_valid retorna la página de una vez
    def form_valid(self, form): #Este método, cuando están validados los campos del csv que se subió (lo cual sucede en el método clean de UploadDelegatesForm), crea a todos los usuarios a partir de los datos que se encuentran en el archivo csv subido.
        return HttpResponse("success")
