# coding=utf-8
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import F, Q
from django.forms.formsets import formset_factory
from django.templatetags.static import static
from models import Evento, Habitacion, User, Persona, Calificacion, Bus
from forms import CalificationFormSet
from io import BytesIO
from reportlab.pdfgen import canvas

#----- TESTS --------#
#These test are for the @user_passes_test decorators
#THey are used to restrict certain views to special groups of users
def conference_check(user):
    """Returns whether the current user is part of the conference team or not."""
    return user.persona.rol.esConference

def jd_check(user):
    """Returns whether the current user is a Jefe de delegación"""
    return user.persona.rol.esJD

@login_required
def index(request):
    """Index view"""
    context = {
        'test': 'pruebaaa'
    }
    return render(request, 'scheduler/index.html', context)

@login_required
def horario(request):
    user = request.user
    persona = user.persona
    eventos = persona.rol.eventos.order_by('horaInicio')
    context = {
        'user': user,
        'eventos': eventos,
    }
    return render(request, 'scheduler/horario.html', context)

@login_required
def horario_conference(request):
    persona_pk = request.user.persona.pk
    rol_pk = request.user.persona.rol.pk
    eventos = Evento.objects.filter(Q(facis__pk=persona_pk)|Q(ocsEncargados__pk=persona_pk)|Q(asistentes__pk=rol_pk)).distinct().order_by('horaInicio')
    context = {'user': request.user, 'eventos':eventos,}
    return render(request, 'scheduler/horario.html', context)

@login_required
def evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    context = {'evento': evento}
    return render(request, 'scheduler/evento.html', context)

@login_required
def habitacion(request):
    habitacion = request.user.persona.habitacion
    context = {'habitacion':habitacion,}
    return render(request, 'scheduler/habitacion.html', context)

@login_required
def habitaciones(request):
    if request.user.persona.rol.esConference:
        habitaciones = Habitacion.objects.order_by('numero')
        context = {'habitaciones':habitaciones,}
        return render(request, 'scheduler/lista_habitaciones.html', context)
    else:
        return render(request, 'scheduler/error_permisos.html')

@login_required
def buses(request):
    if request.user.persona.rol.esConference:
        buses = Bus.objects.order_by('placa')
        context = {'buses':buses,}
        return render(request, 'scheduler/buses.html', context)
    else:
        return render(request, 'scheduler/error_permisos.html')

@login_required
def lista_usuarios(request):
    if request.user.persona.rol.esConference:
        usuarios = User.objects.all()
    else:
        usuarios = User.objects.filter(persona__esPrivado=False)
    context = {'usuarios':usuarios}
    return render(request, 'scheduler/lista_usuarios.html', context)

@login_required
def persona(request, pk):
    persona = Persona.objects.get(pk=pk)
    if request.user.persona.rol.esConference or not persona.esPrivado:
        context = {'persona':persona}
        return render(request,'scheduler/persona.html', context)
    else:
        return render(request, 'scheduler/error_permisos.html')

@login_required
def registrar(request, pk):
    persona = Persona.objects.get(pk=pk)
    if(request.user.persona.rol.esConference):
        if request.method == 'POST':
            persona.estaRegistrado = True
            persona.save()
            return HttpResponseRedirect(request.path)
        else:
            context = {'persona':persona}
            return render(request, 'scheduler/registrar.html', context)
    else:
        return render(request, 'scheduler/error_permisos')

@login_required
def feedback(request):
    if request.method == 'POST':
        pass
    else:
        if(request.user.persona.rol.esJD):
            initValues=[]
            eventos = Evento.objects.all()
            for evento in eventos:
                dicit = {}
                dicit['evento'] = evento
                dicit['lc'] = request.user.persona.lc
                initValues.append(dicit)
            print initValues
            CFormSet = CalificationFormSet(len(initValues))
            formset = CFormSet(initial=initValues, queryset=Calificacion.objects.none())
            return render(request, 'scheduler/feedback.html', {'formset': formset})
        else:
            return render(request, 'scheduler/error_permisos.html')

@login_required
def feedback_form(request):
    if request.method == 'POST':
        pass
    else:
        formset = CalificacionFormSet()
    return render(request, 'scheduler/feedback.html', {'formset': formset})

@login_required
def asistentes_evento(request, pk):
    pass #TODO

@login_required
def inscribir_evento(request, pk):
    if request.method == 'POST':
        evento = Evento.objects.get(pk=pk)
        context = {'evento': evento}
        return render (request, 'scheduler/inscribir_evento.html', context)
    else:
        return HttpResponse("bad request") #TODO

@login_required
@user_passes_test(conference_check, login_url=reverse_lazy('scheduler:error_permisos'))
def escarapelas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="somefilename.pdf"'
    
    buffer = BytesIO()

    p = canvas.Canvas(buffer, pagesize=(343,491))

    url = '/home/camilo/django/natco2015/scheduler'+static('scheduler/img/EscarapelaTemplate.png')
    personas = Persona.objects.all()
    for persona in personas:
        p.drawImage(url, 0, 0)
        p.drawString(100, 373, persona.user.first_name+ ' ' + persona.user.last_name)
        p.drawString(86, 319, persona.lc.nombre)
        p.drawString(82, 242, persona.area)
        p.drawString(236, 242, persona.cargo)
        print persona.qrRegistro.path
        p.drawInlineImage(persona.qrRegistro.path, 103,32, 170, 170)
        p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def error_permisos(request):
    """Show the user an error page if they try to access a page they shouldn't"""
    return render(request, 'scheduler/error_permisos.html')
