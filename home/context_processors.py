from django.utils import tree
from animate import animation_classes
from random import choice
from django.conf import settings

def animations(request):
    return {
        'animation_class': choice(animation_classes)
    }
def baseUrl(request):
    return {
        'BASE_URL': settings.BASE_URL
    }
def roll(request):
    if(not request.user.is_student and request.user.is_staff == False):
        return {
            'is_student': False,
            'is_staff': False,
        }
    if(request.user.is_student):
        return {
            'is_student': True, 
            'is_staff': False,
        }
    if(request.user.is_staff):
        return {
            'is_staff': True,
            'is_student': False, 
        }
