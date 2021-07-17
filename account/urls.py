from django.urls import path
from django.urls.conf import include
from account import views

urlpatterns = [
    path('', views.accounts),
    path('logout/', views.logoutUser),
    path('login/', views.loginUser),
    path('signup/', views.signup),
]
