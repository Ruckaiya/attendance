from django.contrib import admin
from home.models import MyUser
# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_verified', 'is_completed', 'timeStamp')
    ordering = ['id']