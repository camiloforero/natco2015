from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('^login/$', 'django.contrib.auth.views.login', name='login'),
    url(
        '^logout/$', 
        'django.contrib.auth.views.logout', 
        {'next_page': '/app/'}, 
        name='logout' ),
    url('^password_change/$', 'django.contrib.auth.views.password_change',
        {'post_change_redirect':'/app/', 'template_name': 'scheduler/change_password.html',}, name='password_change'),
    url(r'^$', views.index, name='index'),
    url(r'^horario/$', views.horario, name='horario'),
    url(r'^horario_admin/$', views.horario_admin, name='horario_admin'),
    url(r'^eventos/(?P<pk>\d+)/$', views.evento, name='evento'),
    url(r'^eventos/inscribir/$', views.lista_inscribir_evento, name='lista_inscribir_evento'),
    url(r'^eventos/(?P<pk>\d+)/editar_descripcion$', views.editar_descripcion, name='editar_descripcion'),
    url(r'^eventos/(?P<pk>\d+)/inscribir$', views.inscribir_evento, name='inscribir_evento'),
    url(r'^eventos/(?P<pk>\d+)/asistentes$', views.asistentes_evento, name='asistentes_evento'),
    url(r'^personas/(?P<pk>\d+)/$', views.persona, name='persona'),
    url(r'^habitacion/$', views.habitacion, name='habitacion'),
    url(r'^habitaciones/$', views.habitaciones, name='lista_habitaciones'),
    url(r'^check_in_status/$', views.check_in_status, name='check_in_status'),
    url(r'^habitaciones_csv/$', views.habitaciones_csv, name='lista_habitaciones_csv'),
    url(r'^buses/$', views.buses, name='buses'),
    url(r'^personas/$', views.lista_usuarios, name='networking'),
    url(r'^personas/(?P<pk>\d+)/registrar$', views.registrar, name='registrar'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^feedback/(?P<fecha>\d{4}-\d{2}-\d{2})/$', views.feedback_form, name='feedback_form'),
    url(r'^vip/$', views.delegadosVIP, name='vip'),
    url(r'^escarapelas/$', views.escarapelas, name='escarapelas'),
    url(r'^escarapelas_vpm/$', views.escarapelas_vpm, name='escarapelas_vpm'),
    url(r'^error_permisos/$', views.error_permisos, name='error_permisos'),
    url(r'^no_registro/$', views.no_registro, name='no_registro'),
    url(r'^mensaje/$', views.mensaje, name='mensaje'),
    url(r'^media\/(?P<path>.*)$', views.media_xsendfile, {
        'document_root': settings.MEDIA_ROOT,
         }),

]

