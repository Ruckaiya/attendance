from dashboard.models import Attendance
from django import template

register = template.Library()


@register.filter
def makeClass(value):
    class_name = ''.join(i for i in value if not i.isdigit())
    class_name = class_name[0:5]
    class_name = class_name.replace(' ', '-')
    class_name = class_name.lower()
    return class_name


@register.filter
def inThisLink(student, link):
    if(student in Attendance.objects.filter(link=link)):
        return student
    else:
        None