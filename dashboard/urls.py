from django.urls import path
from django.urls.conf import include
from dashboard import views

urlpatterns = [
    path('', views.dashboard),
    path('links/', views.links),
    path('links/<str:slug>/<int:id>/', views.links),
    path('classes/<str:slug>/<int:id>/', views.classes),
    path('classes/', views.classes),
    path('students/', views.students),
    path('students/<int:id>/', views.students),

]
