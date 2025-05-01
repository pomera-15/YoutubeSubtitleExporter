from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
    path('', views.home, name='homepage'),
]