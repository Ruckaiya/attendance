from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
 
    
    path('profile/', views.profile),
    path('profile/<int:id>/', views.profile),
    path('profile/edit/', views.editProfile),
    path('my-attendance/', views.myAttendance),


]
