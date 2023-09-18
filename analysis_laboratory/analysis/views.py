from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .forms import ProductFomrs,LaboratinsFomrs

# Create your views here.


def calculer_moyennes(request):
    moyennes = ProductAnalyse.objects.values('product_name', 'type_produit', 'type_analyse').annotate(
        moyenne_resultat=Avg('resultat')
    )
    

    context = {'moyennes': moyennes}
    return render(request, 'analysis/analyse.html', context)




def home(request):
     Engrais=ProductEngrais.objects.all()
     analysis = ProductAnalyse.objects.all()
     laboratinss=Laborantins.objects.all()
     resultat = Resultat.objects.order_by('-date_analyse')[:5]
     echantillon=Echantillon.objects.all()
     analyse = ProductAnalyse.objects.filter(status='encour')
     analyse1 = ProductAnalyse.objects.filter(status='realise')
     total_laboratins=laboratinss.count()
     total_analyse_encours=analyse.count()
     total_analyse=analysis.count()
     total_analyse_realise=analyse1.count()


 



     context={'Engrais':Engrais,'laboratinss':laboratinss, 'analyse1':analyse1,
               'resultat':resultat,   'echantillon':echantillon , 
                   'analyse':analyse    , 'total_laboratins':  total_laboratins,
                   'total_analyse_encours': total_analyse_encours,
                    'total_analyse':total_analyse ,
                    'total_analyse_realise': total_analyse_realise }
     return render (request ,'analysis/dashboard.html',context)

def laboratins(request, pk_test):
     laboratins=Laborantins.objects.get(id=pk_test)
     analyse= laboratins.productanalyse_set.all()
     analyse_count=analyse.count()
     context={'laboratins': laboratins , 'analyse':analyse,'analyse_count': analyse_count }
     
     return render (request ,'analysis/laboratins.html',context)

# def (request):
#      laboratins=Laborantins.objects.all()
#      context={'laboratins':laboratins}

def createchantillon(request):
     form= ProductFomrs()
     if request.method =='POST':
          form=ProductFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
          #print('Printing POST ', request.POST)
     
     context={'form':form}
     return render (request, 'analysis/echantillon_form.html',context)



def createlaboratins(request):
     form= LaboratinsFomrs()
     if request.method =='POST':
          form=LaboratinsFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
          #print('Printing POST ', request.POST)
     
     context={'form':form}
     return render (request, 'analysis/laboratins_form.html',context)

def analyse(request):
     analyse = ProductAnalyse.objects.all()
     analyse1 = ProductAnalyse.objects.filter(status='encour')
     

    
     

     return render (request ,'analysis/list_analyse.html',{'analyse':analyse ,'analyse1':analyse1})

# @receiver(post_save, sender=ProductAnalyse)
# def calculer_moyenne(sender, instance, **kwargs):
#     # Calculez la somme et le nombre d'analyses pour le type de produit et le type d'analyse de cette instance
#     somme_resultat = ProductAnalyse.objects.filter(
#         type_produit=instance.type_produit,
#         type_analyse=instance.type_analyse
#     ).aggregate(sum('resultat'))['resultat__sum']

#     nombre_analyses = ProductAnalyse.objects.filter(
#         type_produit=instance.type_produit,
#         type_analyse=instance.type_analyse
#     ).count()

#     # Calculez la moyenne
#     if somme_resultat is not None and nombre_analyses > 0:
#         moyenne = somme_resultat / nombre_analyses
#     else:
#         moyenne = 0

#     # Enregistrez la moyenne dans le modèle MoyenneAnalyse
#     MoyenneAnalyse.objects.create(
#         type_produit=instance.type_produit,
#         type_analyse=instance.type_analyse,
#         moyenne=moyenne,
#         date=instance.date_created.date()  # Utilisez la date de création de l'instance
#     )
