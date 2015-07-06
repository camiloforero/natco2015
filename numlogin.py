from scheduler.models import User
from django.db.models import Q

def reporteLogin():
    total = User.objects.filter(persona__delegadoNatco=True, persona__rol__esConference=False).count()
    login = User.objects.filter(persona__delegadoNatco=True, last_login__isnull=False, persona__rol__esConference=False).count()
    return "De %d usuarios, %d han hecho login y %d no" % (total, login, total-login)
