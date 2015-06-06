from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^horario/$', views.horario, name='horario'),
    url(r'^horario_conference/$', views.horario_conference, name='horario_conference'),
    url(r'^eventos/(?P<pk>\d+)/$', views.evento, name='evento'),
    url(r'^eventos/(?P<pk>\d+)/inscribir$', views.inscribir_evento, name='inscribir_evento'),
    url(r'^eventos/(?P<pk>\d+)/asistentes$', views.asistentes_evento, name='asistentes_evento'),
    url(r'^personas/(?P<pk>\d+)/$', views.persona, name='persona'),
    url(r'^habitacion/$', views.habitacion, name='habitacion'),
    url(r'^habitaciones/$', views.habitaciones, name='lista_habitaciones'),
    url(r'^buses/$', views.buses, name='buses'),
    url(r'^personas/$', views.lista_usuarios, name='networking'),
    url(r'^personas/(?P<pk>\d+)/registrar$', views.registrar, name='registrar'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^feedback/(?P<fecha>\d\d)/$', views.feedback_form, name='feedback_form'),
    url(r'^escarapelas/$', views.escarapelas, name='escarapelas'),
    url(r'^error_permisos/$', views.error_permisos, name='error_permisos'),
        

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

