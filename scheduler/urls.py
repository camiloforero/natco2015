from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^horario/$', views.horario, name='horario'),
    url(r'^evento/(?P<pk>\d+)/$', views.evento, name='evento'),
    url(r'^habitacion/$', views.habitacion, name='habitacion'),
    url(r'^lista_habitaciones/$', views.lista_habitaciones, name='lista_habitaciones'),
        

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

