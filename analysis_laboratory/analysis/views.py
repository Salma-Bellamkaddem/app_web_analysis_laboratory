from django.shortcuts import render
from  django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
     laboratinss=Laborantins.objects.all()
     resultat=Resultat.objects.all()
     echantillon=Echantillon.objects.all()

     context={'laboratinss':laboratinss,'resultat':resultat,'echantillon':echantillon}
     return render (request ,'analysis/dashboard.html',context)

def laboratins(request):
     return render (request ,'analysis/laboratins.html')

def analyse(request):
     analyse = ProductAnalyse.objects.all()

     return render (request ,'analysis/analyse.html',{'analyse':analyse})