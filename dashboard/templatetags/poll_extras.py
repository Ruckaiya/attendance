from dashboard.models import Attendance, Class
from django import template
from django.utils import timezone
import datetime
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

@register.filter
def getAttendance(student, data):
    data = data.split(',')
    class_name = Class.objects.filter(name=data[1]).first()
    date = datetime.datetime.strptime(data[0], '%Y-%m-%d')
    attendance = Attendance.objects.filter(student=student, link__class_name=class_name, attendance_date=date)
    if(len(attendance) != 0):
        return "P"
    else:
        return "A"

@register.filter
def getValues(date, selectedClass):
    data = f"{date},{selectedClass}"
    return data


@register.filter
def isExpired(link):
    return (link.expiry - timezone.now()).total_seconds() > 0



@register.simple_tag
def define(val=None):
  return val