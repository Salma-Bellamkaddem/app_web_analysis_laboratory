from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    # path('laboratins/',views.laboratins, name='laboratins'),
    path('laboratins_profile/<int:pk_test>/',views.laboratins, name='laboratins'),
    path('createProductAnalyse/<str:pk>/',views.createProductAnalyse, name="createProductAnalyse"),


    path('analyse/',views.analyse, name="analyse"),
    path('create_analyse/', views.createAnalyse,name="create_analyse"),
     path('update_analyse/<str:pk>/', views.updateAnalyse,name="update_analyse"),
     path('delete_analyse/<str:pk>/', views.deleteAnalyse,name="delete_analyse"),
    

     path('echantillon/',views.echantillon, name="echantillon"),
    path('create_chantillon/', views.createchantillon ,name="createchantillon"),
    path('update_Echantillon/<str:pk>/', views.updateEchantillon ,name="update_Echantillon"),
    path('delete_Echantillon/<str:pk>/', views.deleteEchantillon,name="delete_Echantillon"),
    
    
    path('create_prelevement/', views.createPrelevement ,name="create_prelevement"),
    path('update_prelevement/<str:pk>/', views.updatePrelevement ,name="update_prelevement"),
    path('delete_prelevement/<str:pk>/', views.deletePrelevement,name="delete_prelevement"),
    

    
    
    path('create_laboratins/', views.createlaboratins ,name="createlaboratins"),

] 