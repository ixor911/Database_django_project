from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loadDatabase', views.loadDatabase, name='loadDatabase'),
    path('createDatabase', views.createDatabase, name='createDatabase'),
    path('getTables', views.getTables, name='getTables')
]
