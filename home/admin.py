from django.contrib import admin
from home.models import MyUser, Profile
# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_verified', 'is_completed', 'timeStamp')
    ordering = ['id']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'age', 'number', 'timeStamp')
    ordering = ['id']
