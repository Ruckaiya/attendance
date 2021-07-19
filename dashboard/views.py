from home.models import MyUser
from django.core import exceptions
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dashboard.models import Attendance, Class, Link, Student
from datetime import  timedelta
from django.utils import timezone
from django.contrib import messages

# Create your views here.


@staff_member_required
def dashboard(request):
    return render(request, 'dashboard/index.html')



@staff_member_required
def links(request, slug=None, id=None):
    if(request.method == 'POST'):
        print('in1')
        class_name = request.POST['class']
        expiry = int(request.POST['expiry'])
        time = request.POST['time'].lower()
        class_name = Class.objects.filter(name=class_name).order_by('-id')
        if(len(class_name) != 0):
            print('in2')

            if(time == 'seconds'):
                expiry = timezone.now() + timedelta(seconds=expiry)
            elif(time == 'minutes'):
                expiry = timezone.now() + timedelta(minutes=expiry)
            elif(time == 'hours'):
                expiry = timezone.now() + timedelta(hours=expiry)
            else:
                expiry = timezone.now() + timedelta(minutes=2)
            try:
                link = Link.objects.create(class_name=class_name.first(), expiry=expiry)
                link.save()
                expiry_time = request.POST['expiry']
                messages.success(request, f"Successfully created a new link for  {expiry_time} {time}.")
                print('in3')
                return redirect('/dashboard/links/')
            except Exception as e:
                print(e)
                messages.error(request, 'Faild to create new link')
                return redirect('/dashboard/links/')
                
        else:
            messages.error(request, 'The class you have selected is not available')
            return redirect('/dashboard/links/')
            



        
    elif(request.method == 'GET'):
        all_links = Link.objects.all().order_by('-id')
        all_classes = Class.objects.all().order_by('-id')
        context = {
            'links': all_links,
            'classes': all_classes,
            'attendance': Attendance.objects.all().order_by('-id'),
        }
        return render(request, 'dashboard/links.html', context)

    
@staff_member_required
def classes(request, slug=None, id=None):
    return HttpResponse("classes")
    

    
@staff_member_required
def studentRequest(request):
    if(request.method == 'GET'):
        students = MyUser.objects.filter(is_student=False, is_staff=False, in_draft=False)
        
        context = {
            'students':students
        }
        
        return render(request, 'dashboard/student-requests.html', context)
    elif(request.method == 'POST'):
        action = request.POST['action']
        id = request.POST['id']
        if(action == 'accept'):
            user = MyUser.objects.filter(id=id)
            if(len(user) != 0):
                user = user.first()
                user.is_student = True
                user.in_draft = False
                user.save()
                student = Student.objects.create(student=user)
                student.save()
                messages.success(request, 'Success fully added to student list.')
                return redirect('/dashboard/students/requests/')
            else:
                messages.error(request, 'This student request is not available..')
                return redirect('/dashboard/students/requests/')  
                
        elif(action == 'reject'):
            user = MyUser.objects.filter(id=id)
            if(len(user) != 0):
                user = user.first()
                user.is_student = False
                user.in_draft = True
                user.save()
                messages.success(request, 'Success fully added to drafts.')
                return redirect('/dashboard/students/requests/')
            else:
                messages.error(request, 'This student request is not available..')
                return redirect('/dashboard/students/requests/')  




@staff_member_required
def students(request, id=None):
    if(request.method == 'GET'):
        students = Student.objects.all()
        print(students)
        studentList = []
        for student in students:
            if(student.student in MyUser.objects.filter(is_active=True, is_student=True, in_draft=False)):
                studentList.append(student)
        context = {
            'students':studentList
        }
        
    return render(request, 'dashboard/students.html', context)


@staff_member_required
def studentDraft(request):
    if(request.method == 'GET'):
        students = MyUser.objects.filter(is_student=False, is_staff=False, in_draft=True)
        context = {
            'students':students
        }
        print(context)
        return render(request, 'dashboard/draft.html', context)
    elif(request.method == 'POST'):
        action = request.POST['action']
        id = request.POST['id']
        if(action == 'add-to-students'):
            user = MyUser.objects.filter(id=id)
            if(len(user) != 0):
                user = user.first()
                user.is_student = True
                user.in_draft = False
                user.save()
                student = Student.objects.create(student=user)
                student.save()
                messages.success(request, 'Success fully added to students.')
                return redirect('/dashboard/students/draft/')
        elif(action == 'delete'):
            pass
        students = MyUser.objects.filter(is_student=False, is_staff=False, in_draft=True)
        context = {
            'students':students
        }
        print(context)
        return render(request, 'dashboard/draft.html', context)

    