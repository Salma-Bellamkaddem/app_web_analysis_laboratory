from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    # path('laboratins/',views.laboratins, name='laboratins'),
    path('laboratins_profile/<int:pk_test>/',views.laboratins, name='laboratins'),

    path('analyse/',views.analyse, name="analyse"),
    path('delete_analyse/',views.deleteAnalyse, name="delete_analyse"),


    path('create_chantillon/', views.createchantillon ,name="createchantillon"),
    path('update_Echantillon/<str:pk>/', views.updateEchantillon ,name="update_Echantillon"),
    path('delete_Echantillon/<str:pk>/', views.deleteEchantillon,name="delete_Echantillon"),
    
    
    
    
    path('create_laboratins/', views.createlaboratins ,name="createlaboratins"),

] 