#coding:utf-8
from __future__ import unicode_literals
from django import forms

class UploadDelegatesForm(forms.Form):
    csv = forms.FileField()

class UploadConferenceForm(forms.Form):
    csv = forms.FileField()

class UploadRoomsForm(forms.Form):
    csv = forms.FileField()
