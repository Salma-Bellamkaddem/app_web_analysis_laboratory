from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import *
from django.db.models.signals import post_save
from .filters import AnalyseFilter
from django.core.paginator import Paginator
from .forms import ProductFomrs,LaboratinsFomrs,AnalyseFomrs,EchantillonFomrs

# Create your views here.


# def calculer_moyennes(request):
#     moyennes = ProductAnalyse.objects.values('product_name', 'type_produit', 'type_analyse').annotate(
#         moyenne_resultat=Avg('resultat')
#     )
    

#     context = {'moyennes': moyennes}
#     return render(request, 'analysis/analyse.html', context)




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
     total_product=Engrais.count()


 



     context={'Engrais':Engrais,'laboratinss':laboratinss, 'analyse1':analyse1,
               'resultat':resultat,   'echantillon':echantillon , 
                   'analyse':analyse    , 'total_laboratins':  total_laboratins,
                   'total_analyse_encours': total_analyse_encours,
                    'total_analyse':total_analyse ,
                    'total_analyse_realise': total_analyse_realise,
                     'total_product': total_product }
     return render (request ,'analysis/dashboard.html',context)



# def (request):
#      laboratins=Laborantins.objects.all()
#      context={'laboratins':laboratins}
#product create update modifier 
def echantillon(request):
       echantillon=Echantillon.objects.all()
       Engrais=ProductEngrais.objects.all()
       
       context={'echantillon':echantillon,'Engrais':Engrais}
       return render (request, 'analysis/echantillon.html',context)

#echantillon update create delete

def createPrelevement(request):
     form= EchantillonFomrs()
     if request.method =='POST':
          form=EchantillonFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('echantillon')
     context={'form':form}
     return render (request, 'analysis/prelevement_form.html',context)


def updatePrelevement(request , pk ):
     Product=Echantillon.objects.get(id=pk)
     form =EchantillonFomrs(instance=Product)
     if request.method =='POST':
          form=EchantillonFomrs(request.POST , instance=Product)
          if form.is_valid():
               form.save()
               return redirect('echantillon')
     
     context={'form':form}
     return render (request, 'analysis/prelevement_form.html',context)



def deletePrelevement(request , pk):
     Product=Echantillon.objects.get(id=pk)
     if request.method == "POST":
          Product.delete()
          return redirect('echantillon')
     context={'item':Product}
     return render (request , 'analysis/delete_prelevement.html',context)

#product create update delete

def createchantillon(request):
     form= ProductFomrs()
     if request.method =='POST':
          form=ProductFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('echantillon')
          #print('Printing POST ', request.POST)
     
     context={'form':form}
     return render (request, 'analysis/echantillon_form.html',context)

def updateEchantillon(request , pk ):
     Product=ProductEngrais.objects.get(id=pk)
     form =ProductFomrs(instance=Product)
     if request.method =='POST':
          form=ProductFomrs(request.POST , instance=Product)
          if form.is_valid():
               form.save()
               return redirect('echantillon')
     
     context={'form':form}
     return render (request, 'analysis/echantillon_form.html',context)

def deleteEchantillon(request , pk):
     Product=ProductEngrais.objects.get(id=pk)
     if request.method == "POST":
          Product.delete()
          return redirect('/')
     context={'item':Product}
     return render (request , 'analysis/delete.html',context)





#laborantins create update modifeir 


def laboratins(request, pk_test):
     laboratins=Laborantins.objects.get(id=pk_test)
     analyse= laboratins.productanalyse_set.all()
     analyse_count=analyse.count()
     myFilter = AnalyseFilter(request.GET, queryset=analyse)
     context={'laboratins': laboratins ,'myFilter':myFilter, 'analyse':analyse,'analyse_count': analyse_count }
     
     return render (request ,'analysis/laboratins.html',context)



def createlaboratins(request):
     form= LaboratinsFomrs()
     if request.method =='POST':
          form=LaboratinsFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('laboratins')
          #print('Printing POST ', request.POST)
     
     context={'form':form}
     return render (request, 'analysis/laboratins_form.html',context)






def createProductAnalyse(request,pk):
     laborantins=Laborantins.objects.get(id=pk)
     form= AnalyseFomrs( initial={'laborantins':laborantins})
     if request.method =='POST':
          form=AnalyseFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
       
       
     context={'form':form ,'laboratins':laboratins}
     return render (request, 'analysis/analyse_form.html',context)











def analyse(request):
     analyse = ProductAnalyse.objects.all()
     myFilter = AnalyseFilter(request.GET, queryset=analyse)
     paginator = Paginator(myFilter.qs,4 )
     page_number = request.GET.get('page')
     page_obj = Paginator.get_page(paginator, page_number)
     
     
     context={'analyse':analyse,'page_obj':page_obj ,'myFilter': myFilter}

     return render (request, 'analysis/analyse.html',context)
     # analyse1 = ProductAnalyse.objects.filter(status='encour')
     # return render (request ,'analysis/list_analyse.html',{'analyse':analyse ,'analyse1':analyse1})


def createAnalyse(request):
    
     form= AnalyseFomrs()
     if request.method =='POST':
          form=AnalyseFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('analyse')
       
       
     context={'form':form}
     return render (request, 'analysis/analyse_form.html',context)


def updateAnalyse(request ,pk ):
         Product=ProductAnalyse.objects.get(id=pk)
         form =AnalyseFomrs(instance=Product)
         if request.method =='POST':
          form=AnalyseFomrs(request.POST , instance=Product)
          if form.is_valid():
               form.save()
               return redirect('analyse')
     
         context={'form':form}
         return render (request, 'analysis/analyse_form.html',context)
      


def deleteAnalyse(request ,pk):
     analyse=ProductAnalyse.objects.get(id=pk)
     if request.method == "POST":
          analyse.delete()
          return redirect('/')
     context={'item':analyse}
     return render (request , 'analysis/deleteAnalyse.html',context)
      
     






