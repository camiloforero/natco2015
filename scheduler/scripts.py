# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import PIL
import StringIO
from django.utils.encoding import force_unicode
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import IntegrityError
from scheduler.models import User, Persona, Rol, LC, Habitacion, Bus

def create_conference(conference_dict):
    cedula = conference_dict["id"]
    email = conference_dict["email"]
    username=email.split("@")[0].lower()
    num = 0
    try:
        while True:
            try:
                newuser = User.objects.create_user(username=username, password=cedula)
                break;
            except IntegrityError:
                num += 1
                username = username+str(num)
        newuser.email = email
        persona = Persona()
        persona.nombre = conference_dict["nombre"].decode('latin-1')
        persona.cedula = cedula 
        #persona.cargo = cargo TODO: ver si voy a tener el cargo o no
        persona.rol= Rol.objects.get_or_create(tipo=conference_dict["rol"])[0]
        persona.celular = conference_dict["celular"]
        persona.esVegetariano = False
        persona.lc = LC.objects.get_or_create(nombre="Conference Team")[0]
        persona.delegadoNatco = True
        persona.user = newuser
        persona.save()
        newuser.save()
        return unicode(persona.nombre) + " se agregó a la lista de delegados a Starway"
    except:
        print unicode(newuser)
        newuser.delete()
        raise

def create_delegate(delegate_dict):
    cedula = delegate_dict["id"].strip()
    if cedula is None or cedula =="":
        return "La persona con nombre %s no tiene cedula" % delegate_dict["nombres"]
    #email = delegate_dict["email"]
    email = "none@none.com"
    #username=email.split("@")[0].lower()
    username = cedula
    try:
        try:
            newuser = User.objects.create_user(username=username, password=cedula)
            newuser.email = email
            persona = Persona()
            persona.nombre=delegate_dict["nombres"].decode('latin-1')

            persona.cedula = cedula 
            #cargo = delegate_dict["rol"] + " " + delegate_dict["area"]
            cargo = "-"
            persona.cargo = cargo
            #persona.area=delegate_dict["area"]
            persona.area = "-"
            #persona.rol= Rol.objects.get_or_create(tipo=delegate_dict["role-rol"])[0]
            persona.rol= Rol.objects.get_or_create(tipo="-")[0]
            try:
                persona.celular = int(delegate_dict["celular"].replace(" ", ""))
            except ValueError:
                persona.celular = 00000000
                
            #persona.esVegetariano = delegate_dict["vegetariano"]
            persona.esVegetariano = False
            #persona.lc = LC.objects.get_or_create(nombre=delegate_dict["lc-comite-local"])[0]
            persona.lc = LC.objects.get_or_create(nombre="-")[0]
            #img_io = getImage(delegate_dict["your-picture-tu-foto"][1])
            #img_file = InMemoryUploadedFile(img_io, None, 'profile', delegate_dict["your-picture-tu-foto"][0], img_io.len, None)
            #persona.foto.save('foto-'+username+'.'+delegate_dict["your-picture-tu-foto"][0].split('/')[1], img_file, save=False)
            persona.delegadoVPM = False
            persona.delegadoNatco = True
            numHabitacion = delegate_dict["habitacion"]
            #torre = delegate_dict["torre"]
            torre = "Hotel Madaura"
            habitacion = Habitacion.objects.get_or_create(torre=torre, numero=numHabitacion)[0]
            persona.habitacion = habitacion
            persona.user = newuser
            persona.save()
            newuser.save()
            return unicode(persona) + " se agregó a la lista de delegados a NATCO"
        except IntegrityError:
         return "El usuario con cédula %s ya existe" % cedula
    except:
        print unicode(newuser)
        print unicode(persona)
        newuser.delete()
        raise

def add_room(room_dict):
    cedula = room_dict["cedula"].split('.')[0]
    try:
        persona = Persona.objects.get(cedula=cedula)
        numHabitacion = room_dict["habitacion"].split(".")[0]
        torre = room_dict["torre"]
        habitacion = Habitacion.objects.get_or_create(torre=torre, numero=numHabitacion)[0]
        persona.habitacion = habitacion
        persona.save()
        return "La persona con nombre %s y cédula %s se le ha asignado satisfactoriamente la habitación %s, torre %s" % (room_dict["nombre"], cedula, numHabitacion, torre) 
    except KeyError:
        return "%s aún no tiene habitación asignada" % persona
    except Persona.DoesNotExist:
        return "La persona con nombre %s y cédula %s no está registrada en este momento. Revisar el caso y solucionar manualmente" % (room_dict["nombre"], cedula) 
        

#==============================================================
def getImage(imageid):
    global client
    rawPhoto = client.Files.find_raw(int(imageid))
    img_io = StringIO.StringIO(rawPhoto)
    return img_io

def getNames(full_name):
    full_name = force_unicode(full_name)
    words = full_name.split()
    if len(words) <= 2:
        return words
    else:
        first_name = words[:2]
        last_name = words[2:]
        return [u' '.join(first_name), u' '.join(last_name)]
    


#for field in fields[0]: print field["external_id"] + str(field["values"][0]["value"])

def cargarBuses(csvfile):
    reader = csv.DictReader(csvfile, dialect='excel')
    for row in reader:
        try:
            persona= Persona.objects.get(cedula=row['id'])
            bus = Bus.objects.get_or_create(pk=row['bus'])[0]
            bus.save()
            persona.bus = bus
            persona.save()
        except Persona.DoesNotExist:
            print "La persona %s %s no está inscrita en la aplicación" % (row['nombre'], row['apellido'])
