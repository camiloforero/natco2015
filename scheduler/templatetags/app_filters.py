from django import template
from django.utils.encoding import force_unicode
from datetime import datetime
register = template.Library()

@register.filter
def truncatewords2(s, num):
    "Truncates a string after a certain number of words."
    s = force_unicode(s)
    length = int(num)
    words = s.split()
    if len(words) > length:
        words = words[:length]
    return u' '.join(words)

@register.filter
def alto(hInicio, hFin):
    #inicio = datetime.strptime(hInicio, "%H:%M")
    #fin = datetime.strptime(hFin, "%H:%M")
    return (hFin - hInicio).seconds / 1800
    
