from home.models import MyUser
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def profile(request, id=None):
    if(request.user.is_staff):
        return  redirect('/dashboard')
    else:
        if(request.method == 'GET'):
            user = request.user
            context = {
                'email': user.email,
                'fName': user.first_name,
                'lName': user.last_name,
                'age': user.age,
                'number': user.number,
                'addNumber': user.addtional_number,
            }
            return render(request, 'home/profile.html', context)
    
@login_required
def editProfile(request):
    if(request.user.is_staff):
        return redirect('/dashboard')
    else:
        if(request.method == 'GET'):
            user = request.user
            context = {
                'email': user.email,
                'fName': user.first_name,
                'lName': user.last_name,
                'age': user.age,
                'number': user.number,
                'addNumber': user.addtional_number,
            }
            print(context)
            return render(request, 'home/edit-profile.html', context)

        elif(request.method == 'POST'):
            request.user.email = request.POST['email']
            request.user.first_name = request.POST['first-name']
            request.user.last_name = request.POST['last-name']
            request.user.age = request.POST['age']
            request.user.number = request.POST['number']
            request.user.addtional_number = request.POST['add-number']
            request.user.save()
            return redirect('/profile/edit/')

@login_required
def myAttendance(request):
    return HttpResponse("myAttendance")