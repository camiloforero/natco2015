from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from models import Evento, Habitacion

@login_required
def index(request):
    context = {
        'test': 'pruebaaa'
    }
    return render(request, 'scheduler/index.html', context)

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/scheduler/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your NATCO account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'scheduler/login.html', {})    

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/scheduler/')    

@login_required
def horario(request):
    user = request.user
    persona = user.persona
    eventos = persona.rol.eventos.order_by('horaInicio')
    context = {
        'user': user,
        'persona':persona,
        'eventos': eventos,
    }
    return render(request, 'scheduler/horario.html', context)

def evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    context = {'evento': evento}
    return render(request, 'scheduler/evento.html', context)

def habitacion(request):
    habitacion = request.user.persona.habitacion
    context = {'habitacion':habitacion,}
    return render(request, 'scheduler/habitacion.html', context)

def lista_habitaciones(request):
    habitaciones = Habitacion.objects.order_by('numero')
    context = {'habitaciones':habitaciones,}
    return render(request, 'scheduler/lista_habitaciones.html', context)
