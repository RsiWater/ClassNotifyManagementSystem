from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home),
    path('rollcall', views.rollcall),
    path('rollcall/send', views.sendRollcall),
    path('homework', views.homework),
    path('homework/send', views.sendHW),
    path('gradeView', views.gradeView)
]