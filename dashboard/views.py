from django.core import exceptions
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dashboard.models import Class, Link
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
            'classes': all_classes
        }
        return render(request, 'dashboard/links.html', context)

    
@staff_member_required
def classes(request, slug=None, id=None):
    return HttpResponse("classes")

    
@staff_member_required
def students(request, id=None):
    return HttpResponse("students")

    