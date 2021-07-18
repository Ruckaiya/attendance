from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required
def index(request):
    if(request.user.is_staff):
        return  redirect('/dashboard')
    return render(request, 'home/index.html')


@login_required
def profile(request, id=None):
    return HttpResponse("profile")
    
@login_required
def editProfile(request):
    return HttpResponse("editProfile")

@login_required
def myAttendance(request):
    return HttpResponse("myAttendance")