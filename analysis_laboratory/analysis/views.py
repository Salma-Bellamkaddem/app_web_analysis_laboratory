from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .models import *
from .decorators import unauthenticated_user
from django.db.models.signals import post_save
from .filters import AnalyseFilter
from django.core.paginator import Paginator
from .forms import CreateUserForm,ProductFomrs,LaboratinsFomrs,AnalyseFomrs,EchantillonFomrs
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from datetime import datetime
#login register forgetpassword 


@login_required(login_url='login')
@admin_only
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





@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + user)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'analysis/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'analysis/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['laborantins'])
def userPage(request):
       
       analysis=request.user.laborantins.productanalyse_set.all()
       total_analyse=analysis.count()
       total_analyse_encours=analysis.filter(status='encour').count()
       total_analyse_realise = analysis.filter(status='realise').count()

       print('ANALYSIS:',analysis)
       context={'analysis':analysis,'total_analyse':total_analyse,
          'total_analyse_encours':total_analyse_encours,'total_analyse_realise':total_analyse_realise}
       return render(request, 'analysis/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['laborantins'])
def accountSettings(request):
	laborantins = request.user.laborantins
	form = LaboratinsFomrs(instance=laborantins)

	if request.method == 'POST':
		form = LaboratinsFomrs(request.POST, request.FILES,instance=laborantins)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'analysis/account_settings.html', context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['laborantins'])
def createAnalysis(request):
    
     form= AnalyseFomrs()
     if request.method =='POST':
          form=AnalyseFomrs(request.POST)
          if form.is_valid():
              product_analyse = form.save(commit=False)
              product_analyse.date_created = datetime.now()
              product_analyse.save()
              return redirect('/')
          else:
            form = AnalyseFomrs()
    
       
       
     context={'form':form}
     return render (request, 'analysis/analyse_form.html',context)






# Create your views here.


# def calculer_moyennes(request):
#     moyennes = ProductAnalyse.objects.values('product_name', 'type_produit', 'type_analyse').annotate(
#         moyenne_resultat=Avg('resultat')
#     )
    

#     context = {'moyennes': moyennes}
#     return render(request, 'analysis/analyse.html', context)






# def (request):
#      laboratins=Laborantins.objects.all()
#      context={'laboratins':laboratins}
#product create update modifier 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def echantillon(request):
       echantillon=Echantillon.objects.all()
       Engrais=ProductEngrais.objects.all()
       
       context={'echantillon':echantillon,'Engrais':Engrais}
       return render (request, 'analysis/echantillon.html',context)

#echantillon update create delete
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createPrelevement(request):
     form= EchantillonFomrs()
     if request.method =='POST':
          form=EchantillonFomrs(request.POST)
          if form.is_valid():
               form.save()
               return redirect('echantillon')
     context={'form':form}
     return render (request, 'analysis/prelevement_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePrelevement(request , pk):
     Product=Echantillon.objects.get(id=pk)
     if request.method == "POST":
          Product.delete()
          return redirect('echantillon')
     context={'item':Product}
     return render (request , 'analysis/delete_prelevement.html',context)

#product create update delete
@login_required(login_url='login')
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEchantillon(request , pk):
     Product=ProductEngrais.objects.get(id=pk)
     if request.method == "POST":
          Product.delete()
          return redirect('/')
     context={'item':Product}
     return render (request , 'analysis/delete.html',context)





#laborantins create update modifeir 
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def laboratins(request, pk_test):
     laboratins=Laborantins.objects.get(id=pk_test)
     analyse= laboratins.productanalyse_set.all()
     analyse_count=analyse.count()
     myFilter = AnalyseFilter(request.GET, queryset=analyse)
     context={'laboratins': laboratins ,'myFilter':myFilter, 'analyse':analyse,'analyse_count': analyse_count }
     
     return render (request ,'analysis/laboratins.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createProductAnalyse(request,pk):
    try:
        laborantins = Laborantins.objects.get(id=pk)
    except Laborantins.DoesNotExist:
        # Gérer le cas où Laborantins avec l'ID spécifié n'existe pas
        return redirect('/')  # Rediriger vers une page d'erreur ou une autre page appropriée
    
    if request.method == 'POST':
        form = AnalyseFomrs(request.POST)
        if form.is_valid():
            product_analyse = form.save(commit=False)
            product_analyse.laborantins = laborantins  # Affectez le laborantins approprié
            product_analyse.date_created = datetime.now()
            product_analyse.save()
            return redirect('/')  # Redirigez vers la page souhaitée après la création
    else:
        form = AnalyseFomrs(initial={'laborantins': laborantins})
    
    context = {'form': form, 'laborantins': laborantins}
    return render(request, 'analysis/analyse_form.html', context)










@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createAnalyse(request):
    
     form= AnalyseFomrs()
     if form.is_valid():
          product_analyse = form.save(commit=False)
          product_analyse.date_created = datetime.now()
          product_analyse.save()
          return redirect('/')
     else:
        form = AnalyseFomrs()
    
       
       
     context={'form':form}
     return render (request, 'analysis/analyse_form.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAnalyse(request ,pk ):
         Product=ProductAnalyse.objects.get(id=pk)
         form =AnalyseFomrs(instance=Product)
         if request.method =='POST':
          form=AnalyseFomrs(request.POST , instance=Product)
          if form.is_valid():
               form.save()
               return redirect('/')
     
         context={'form':form}
         return render (request, 'analysis/analyse_form.html',context)
      
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteAnalyse(request ,pk):
     analyse=ProductAnalyse.objects.get(id=pk)
     if request.method == "POST":
          analyse.delete()
          return redirect('/')
     context={'item':analyse}
     return render (request , 'analysis/deleteAnalyse.html',context)
      
     





