from django.contrib import admin
from dashboard.models import Student, Class, Link, Attendance

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'timeStamp')
    ordering = ['id']


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time',  'timeStamp')
    ordering = ['id']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'token', 'code', 'timestamp', 'expiry')
    ordering = ['id']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student',  'attendance_date', 'attendance_time', 'link')
    ordering = ['id']
