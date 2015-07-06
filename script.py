# -*- coding: utf-8 -*-
from pypodio2 import api
import csv
import PIL
import StringIO
from django.utils.encoding import force_unicode
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import IntegrityError
from scheduler.models import User, Persona, Rol, LC, Habitacion, Bus
CLIENT_ID = "natco2015"
CLIENT_SECRET = "6FHzzKdpWDz3UpBJzxRgaIHM88wqQZR6eIN2Q9v31UbdvqWvl9fnZL4Xo3xpROfy"
#APP_ID = "12485061" 
#APP_TOKEN = "80705c5b68194145802eda3e76879267"
APP_ID = "12436627"
APP_TOKEN = "adcfb4d7c53c4f539bc416c989b70b93"
#APP_ID = "12448603"
#APP_TOKEN = "045833b5b1ed43d7bacce82145514ae9"
client = None

def startClient():
    global client
    if client==None:
        client = api.OAuthAppClient(CLIENT_ID, CLIENT_SECRET, APP_ID, APP_TOKEN)

def getDict():
    global client
    startClient()
    items = client.Item.filter(
        int(APP_ID),{
            'limit': 400, 
            'filters':[{
                "key":"96943879",
                "values":[1],
            }],
        },
    )["items"]
    fields = [makeDict(item) for item in items]
    return fields

def makeDict(item):
    dictionary = dict([ (field["external_id"], getFieldValue(field)) for field in item["fields"] ])
    return dictionary

def getFieldValue(field):
    if field["type"] == "category":
        return field["values"][0]["value"]["text"]
    elif field["type"] == "image":
        return [field["values"][0]["value"]["mimetype"], field["values"][0]["value"]["file_id"]]
    else:
        return field["values"][0]["value"]

def createUser(user_dict):
    startClient()
    cedula = user_dict["number-numero"].split('.')[0]
    try:
        persona = Persona.objects.get(cedula=cedula)
        persona.delegadoNatco = True
        persona.save()
    except Persona.DoesNotExist:
        email = user_dict["e-mail-correo-electronico"]
        username=email.split("@")[0]
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
            newuser.first_name=user_dict["name-nombre"]
            newuser.last_name=user_dict["last-names-apellidos"]
            persona = Persona()
            persona.cedula = cedula 
            cargo = user_dict["role-rol"] + " " + user_dict["area-area"]
            persona.cargo = cargo
            persona.area=user_dict["area-area"]
            persona.rol= Rol.objects.get_or_create(tipo=user_dict["role-rol"])[0]
            persona.celular = user_dict["mobile-phone-celular"].split(".")[0]
            persona.esVegetariano = user_dict["diet-restrictions-restricciones-alimenticias"]
            persona.lc = LC.objects.get_or_create(nombre=user_dict["lc-comite-local"])[0]
            img_io = getImage(user_dict["your-picture-tu-foto"][1])
            #img_file = InMemoryUploadedFile(img_io, None, 'profile', user_dict["your-picture-tu-foto"][0], img_io.len, None)
            #persona.foto.save('foto-'+username+'.'+user_dict["your-picture-tu-foto"][0].split('/')[1], img_file, save=False)
            persona.delegadoVPM = False
            persona.delegadoNatco = True
            persona.user = newuser
            persona.save()
            newuser.save()
            print str(persona.user) + "'se agregó a la lista de delegados a NATCO"
        except:
            print str(newuser)
            newuser.delete()
            raise

def addRoom(user_dict):
    startClient()
    cedula = user_dict["number-numero"].split('.')[0]
    try:
        persona = Persona.objects.get(cedula=cedula)
        numHabitacion = user_dict["cuarto-2"].split(".")[0]
        torre = user_dict["cuarto"]
        habitacion = Habitacion.objects.get_or_create(torre=torre, numero=numHabitacion)[0]
        persona.habitacion = habitacion
        persona.save()
    except KeyError:
        print "%s aún no tiene habitación asignada" % persona
    except Persona.DoesNotExist:
        print "La persona con nombre %s %s y cédula %s no está registrada en este momento. Revisar el caso y solucionar manualmente" % (user_dict["name-nombre"], user_dict["last-names-apellidos"], cedula) 
        

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
