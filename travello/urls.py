from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', views.api, name="calc"),
    path('api/add/', views.add, name="calc")
]
