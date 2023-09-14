from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('laboratins/',views.laboratins),
    path('analyse/',views.analyse),
]