from django.urls import path
from django.urls.conf import include
from dashboard import views

urlpatterns = [
    path('', views.dashboard),
]