from animate import animation_classes
from random import choice

def animations(request):
    return {
        'animation_class': choice(animation_classes)
    }