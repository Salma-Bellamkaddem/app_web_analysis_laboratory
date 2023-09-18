from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    # path('laboratins/',views.laboratins, name='laboratins'),
    path('laboratins_profile/<int:pk_test>/',views.laboratins, name='laboratins'),
    path('analyse/',views.analyse, name="analyse"),
    path('createchantillon/', views.createchantillon ,name="createchantillon"),
     path('createlaboratins/', views.createlaboratins ,name="createlaboratins"),

] 