# coding=utf-8
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F, Q
from django.forms.formsets import formset_factory
from django.templatetags.static import static
from django.utils import timezone
from models import Evento, Habitacion, User, Persona, Calificacion, Bus
from forms import CalificationFormSet, EncuestaForm, EventoFileForm, EventoDescripcionForm
from django.conf import settings
from datetime import datetime, time, timedelta, date
from io import BytesIO
from reportlab.pdfgen import canvas
import csv
import os

#----- TESTS --------#
#These test are for the @user_passes_test decorators
#THey are used to restrict certain views to special groups of users
def conference_check(user):
    """Returns whether the current user is part of the conference team or not."""
    return user.persona.rol.esConference

def jd_check(user):
    """Returns whether the current user is a Jefe de delegación"""
    return user.persona.esJD

def registrado_check(user):
    """Returns whether the current user has registered or not"""
    return user.persona.estaRegistrado

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def index(request):
    """Index view"""
    context = {
        'test': 'pruebaaa'
    }
    return render(request, 'scheduler/index.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def horario(request):
    persona = request.user.persona
    persona_pk = persona.pk
    rol = persona.rol
    tipoRol = rol.tipo
    if(tipoRol=="OC"):
        eventos = Evento.objects.filter(ocsEncargados__pk=persona_pk).prefetch_related('facis__user', 'ocsEncargados__user').select_related('tipo')
    elif(tipoRol=="FACI" or tipoRol=="Chair"):
        eventos = Evento.objects.filter(facis__pk=persona_pk).prefetch_related('facis__user', 'ocsEncargados__user').select_related('tipo')
    else:
        eventos1 = rol.eventos.order_by('horaInicio').prefetch_related('facis__user', 'ocsEncargados__user').select_related('tipo')
        eventos2 = persona.eventos.order_by('horaInicio').prefetch_related('facis__user', 'ocsEncargados__user').select_related('tipo')
        eventos = eventos1 | eventos2

    context = {'eventos':eventos,}
    return render(request, 'scheduler/horario.html', context)

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def horario_admin(request):
    eventos = Evento.objects.all().order_by('horaInicio').prefetch_related('facis__user', 'ocsEncargados__user').select_related('tipo')
    tiempos = []
    horaInicio1 = datetime.combine(date.today(), time(6, tzinfo=timezone.get_default_timezone()))
    horaInicio2 = datetime.combine(date.today(), time(6, 30, tzinfo=timezone.get_default_timezone()))
    for i in range(0, 36):
        tiempos.append([(horaInicio1 + i*timedelta(minutes=30)).time(), (horaInicio2 + i*timedelta(minutes=30)).time()])

    context = {'user': request.user, 'eventos':eventos, 'tiempos': tiempos,}
    return render(request, 'scheduler/horario_admin.html', context)

@login_required
def horario_vpm(request):
    agendas = ("PM", "IGCDP", "OGCDP", "IGIP", "OGIP", "TM", "S&S", "FL&M", "MKT")
    context = {"sesiones":agendas}
    return render(request, 'scheduler/horarios_vpm.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        fileform = EventoFileForm(request.POST, request.FILES, instance=evento)
        if fileform.is_valid():
            fileform.save()
        else:
            return HttpResponse(str(fileform.errors))
    context = {'evento': evento}
    if request.user.persona.rol.esConference:
        fileform = EventoFileForm()
        context['form'] = fileform
    return render(request, 'scheduler/evento.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def habitacion(request):
    """Allows to see the information of the current user's room"""
    habitacion = request.user.persona.habitacion
    context = {'habitacion':habitacion,}
    return render(request, 'scheduler/habitacion.html', context)

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def habitaciones(request):
    habitaciones = Habitacion.objects.all().prefetch_related('ocupantes__user', 'ocupantes__lc').order_by('numero')
    context = {'habitaciones':habitaciones,}
    return render(request, 'scheduler/lista_habitaciones.html', context)

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def habitaciones_csv(request):
    habitaciones = Habitacion.objects.all().prefetch_related('ocupantes__user', 'ocupantes__lc').order_by('numero')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="habitaciones.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    for habitacion in habitaciones:
        for persona in habitacion.ocupantes.all():
            writer.writerow([persona.habitacion.numero, persona.user.first_name.encode('utf-8') + " " + persona.user.last_name.encode('utf-8'), persona.lc.nombre.encode('utf-8'), unicode(persona.celular)])

    return response 

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def buses(request):
    buses = Bus.objects.order_by('placa')
    context = {'buses':buses,}
    return render(request, 'scheduler/buses.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def lista_usuarios(request):
    if request.user.persona.rol.esConference:
        usuarios = User.objects.all().order_by('persona__lc__nombre').select_related('persona__lc', 'persona__rol')
    else:
        usuarios = User.objects.filter(persona__esPrivado=False).order_by('persona__lc__nombre').select_related('persona__lc', 'persona__rol')

    context = {'usuarios':usuarios}
    return render(request, 'scheduler/networking.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def persona(request, pk):
    persona = Persona.objects.select_related('user', 'lc', 'rol').get(pk=pk)
    if request.user.persona.rol.esConference or not persona.esPrivado:
        context = {'persona':persona}
        return render(request,'scheduler/persona.html', context)
    else:
        return render(request, 'scheduler/error_permisos.html')

@login_required
def registrar(request, pk):
    if request.user.persona.rol.esConference:
        persona = Persona.objects.select_related('user').get(pk=pk)
        if request.method == 'POST':
            numMaletas = request.POST.get("numMaletas")
            persona.numMaletas = int(numMaletas)
            persona.estaRegistradoVPM = True
            persona.save()
            return HttpResponseRedirect(request.path)
        else:
            context = {'persona':persona}
            return render(request, 'scheduler/registrar.html', context)

    else:
        return HttpResponseRedirect(reverse("scheduler:persona", kwargs={'pk':pk}))

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def check_in_status(request):
    usuarios = User.objects.filter(persona__rol__esConference=False, persona__delegadoVPM=True).order_by('persona__estaRegistradoVPM', 'persona__lc__nombre').select_related('persona__lc')
    context = {'usuarios':usuarios, 'evento':'VPM'}
    return render(request, 'scheduler/check_in_status.html', context)
            
@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
@user_passes_test(jd_check, login_url=reverse_lazy('scheduler:error_permisos'))
def feedback_form(request, fecha):
    fechaActual = datetime.strptime(fecha, "%Y-%m-%d")
    print fechaActual
    if request.method == 'POST':
        CFormSet = CalificationFormSet(0)
        formset = CFormSet(request.POST, prefix="calificaciones")
        return HttpResponse(formset)
    else:
        rangoFecha = (
        datetime.combine(fechaActual, datetime.min.time()),
        datetime.combine(fechaActual, datetime.max.time())
        )
        initValues=[]
        eventos = Evento.objects.filter(horaInicio__range=rangoFecha)
        for evento in eventos:
            dicit = {}
            dicit['evento'] = evento.nombre
            dicit['lc'] = request.user.persona.lc
            initValues.append(dicit)
        CFormSet = CalificationFormSet(len(initValues))
        formset = CFormSet(initial=initValues, queryset=Calificacion.objects.none(), prefix="calificaciones")
        eform = EncuestaForm(prefix="encuesta")
        context = {'formset': formset, 'eform': eform}
        return render(request, 'scheduler/feedback_form.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
@user_passes_test(jd_check, login_url=reverse_lazy('scheduler:error_permisos'))
def feedback(request):
    fechas = Evento.objects.datetimes('horaInicio', 'day')
    context = {'fechas':fechas}
    return render(request, 'scheduler/feedback.html', context)

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def asistentes_evento(request, pk):
    pass #TODO

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def lista_inscribir_evento(request):
    eventos = Evento.objects.filter(tipo__esInscribible=True).order_by('horaInicio').select_related('tipo')
    context = {'eventos':eventos}
    return render(request, 'scheduler/lista_inscribir_evento.html', context)

@login_required
@user_passes_test(registrado_check, login_url=reverse_lazy('scheduler:no_registro'))
def inscribir_evento(request, pk):
    if request.method == 'POST':
        persona = request.user.persona
        evento = Evento.objects.get(pk=pk)
        evento2 = None
        pk2 = request.POST.get('pk2', None)
        if pk2: #La forma de agregar evento pide una confirmación de sobre escritura, y envía como parámetro la llave primaria del evento que será reemplazado
            agregado = True
            evento2 = Evento.objects.get(pk=pk2)
            evento2.pAsistentes.remove(persona)
            evento2.save()
        else:
            hi = evento.horaInicio
            hf = evento.horaFin
            try:
                evento2 = Evento.objects.get(horaInicio__lt=hf, horaFin__gt=hi, pAsistentes__pk=request.user.persona.pk)
                agregado = False
            except Evento.DoesNotExist:
                agregado = True

        if agregado:
            evento.pAsistentes.add(persona)
            evento.save()
        context= {'evento': evento, "evento2": evento2, 'agregado':agregado}
        return render (request, 'scheduler/inscribir_evento.html', context)
    else:
        return HttpRedirect(reverse("scheduler:evento", kwargs={'pk':pk})) #TODO

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def editar_descripcion(request, pk):
    evento = Evento.objects.get(pk=pk)
    form = EventoDescripcionForm(instance=evento)
    if request.method == 'POST':
        form = EventoDescripcionForm(request.POST, instance = evento)
        form.save()
        return redirect('scheduler:evento', pk=pk)
    else:
        context = {'evento':evento, 'form':form}
        return render (request, 'scheduler/editar_descripcion.html', context)

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def escarapelas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="escarapelas_natco.pdf"'
    
    buffer = BytesIO()

    p = canvas.Canvas(buffer, pagesize=(709,788))

    url = settings.STATIC_ROOT + 'scheduler/img/escarapela_back_template.png'
    personas = Persona.objects.filter(Q(rol__esConference=True))
    for persona in personas:
        #p.setFont('Helvetica', 20)
        p.drawImage(url, 0, 0)
        #p.drawCentredString(295, 387, persona.user.first_name.split(' ')[0] + ' ' + persona.user.last_name.split(' ')[0])
        #p.drawCentredString(574, 299, persona.rol.tipo)
        #p.drawCentredString(551, 387, persona.lc.nombre)
        #p.drawCentredString(296, 299, persona.cargo)
        #p.drawInlineImage(persona.qrRegistro.path, 263, 45, 183, 183)
        p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def escarapelas_vpm(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="escarapelas_vpm.pdf"'
    
    buffer = BytesIO()

    p = canvas.Canvas(buffer, pagesize=(953,1364))

    url = settings.STATIC_ROOT + 'scheduler/img/escarapela_vpm_template.png'
    personas = Persona.objects.filter(rol__esConference=True)
    #for persona in personas:
    p.setFont('Helvetica', 25)
    p.drawImage(url, 0, 0)
    #p.drawCentredString(402, 805, persona.user.first_name+ ' ' + persona.user.last_name)
    #p.drawCentredString(779, 805, persona.lc.nombre)
    #p.drawCentredString(814, 676, persona.rol.tipo)
    #p.drawCentredString(402, 676, persona.cargo)
    #print persona.qrRegistro.path
    #p.drawInlineImage(persona.qrRegistro.path, 235,61, 472, 472)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def error_permisos(request):
    """Show the user an error page if they try to access a page they shouldn't"""
    return render(request, 'scheduler/error_permisos.html')
    
def no_registro(request):
    """Show the user an error page if they try to access a page they shouldn't"""
    return render(request, 'scheduler/no_registro.html')

def mensaje(request, mensaje):
    return render(request, 'scheduler/mensaje.html', {'mensaje':mensaje})

def delegadosVIP(request):
    """Show the 5 people with the most VIP points"""
    delegados = Persona.objects.all().order_by("-puntos")[:5]
    context = {"delegados": delegados}
    return render(request, "scheduler/delegadosVIP.html", context)

@login_required
def media_xsendfile(request, path, document_root):
    response = HttpResponse()
    response['Content-Type'] = ''
    response['X-Sendfile'] = (os.path.join(document_root, path)).encode('utf-8')
    return response
