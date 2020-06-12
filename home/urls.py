from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home),
    path('rollcall', views.rollcall),
    path('homework', views.homework),
    path('gradeView', views.gradeView),
    path('studentManage', views.studentManage)
]