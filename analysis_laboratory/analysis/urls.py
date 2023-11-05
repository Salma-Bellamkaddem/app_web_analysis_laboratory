from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404 ,handler500,handler400



urlpatterns = [
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('export-pdf',views.generate_pdf,name="export-pdf"),
    




    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
     path('create_analysis/', views.createAnalysis, name="create_analysis"),
      path('account/', views.accountSettings, name="account"),
    
    
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





     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="analysis/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="analysis/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="analysis/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="analysis/password_reset_done.html"), 
        name="password_reset_complete"),
    

] 

handler404 = 'analysis.views.error_404'
handler500='analysis.views.error_500'
handler400='analysis.views.error_400'