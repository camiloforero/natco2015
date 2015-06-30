from scheduler.models import User
from django.db.models import Q

def reporteLogin():
    total = User.objects.all().count()
    login = User.objects.filter(~Q(last_login=None)).count()
    return "De %d usuarios, %d han hecho login y %d no" % (total, login, total-login)
