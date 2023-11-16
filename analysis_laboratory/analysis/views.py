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
      
     




from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import ProductAnalyse
from reportlab.platypus.flowables import HRFlowable  # Ajoutez cette ligne d'importation



def generate_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file" and specifying the page size (e.g., letter).
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create a list to hold the content elements of the PDF.
    elements = []
    # Ajoutez l'en-tête au contenu.
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    elements.append(Paragraph(f"Date: {formatted_date}", getSampleStyleSheet()['Heading1']))

    # Add a spacer for separation.
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    # Add the date to the content.
     # Add the company logo to the content.
    logo_path = "static/images/logo.png"  # Replace with the path to your company's logo image.
    logo = Image(logo_path, width=90, height=70)
    elements.append(logo)

    header_text = """
    "OCP SA
    Direction opérations industrielles
    Direction site Jorf Lasfar
    Laboratoire central"
   
   
    """
    header_style = getSampleStyleSheet()['Heading4']
    elements.append(Paragraph(header_text, header_style))

    # Ajoutez une ligne horizontale pour séparer la section du logo du reste du contenu.
    elements.append(Spacer(1, 12))


   

    # Ajoutez une ligne horizontale pour séparer la section `analysis.location` du tableau.
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.black))


    # Add the company name to the content.
    elements.append(Paragraph(" Rapport d'essai ", getSampleStyleSheet()['Heading1']))

   

    # Fetch your analysis data from the database and format it into a list of lists for the table.
    # Replace 'YourAnalysisModel' with your actual model name and customize the data retrieval.
    analysis_data = ProductAnalyse.objects.all()
  # Add the date to the content.
    selected_date = request.POST.get('date')  # Récupérez la date sélectionnée depuis le formulaire.
    elements.append(Paragraph(f"Date: {selected_date}", getSampleStyleSheet()['Heading1']))
    
    # Fetch your analysis data based on the selected date.
    formatted_date = datetime.strptime(selected_date, "%Y-%m-%d")
    analysis_data = ProductAnalyse.objects.filter(date_created=formatted_date)
    
    # Create the header row with field names.
    header_row = [  "Location","Product Name", "Type de Produit", "Type d'Analyse", "Heure de Création", "Résultat"]
    data = [header_row]

    # Create rows with data.
    for analysis in analysis_data:
        row = [  analysis.location,analysis.product_name, analysis.type_produit, analysis.type_analyse,  analysis.date_created.strftime('%H:%M'),analysis.resultat]
        data.append(row)

    # Create the table and set its style.
    table = Table(data, colWidths=[100, 100, 100, 100, 100]) 



    
    table_style = [
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
      ]
    
    text_style = [
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
      ]
    # Appliquez les styles à la table.
    table.setStyle(table_style)
    table.setStyle(text_style)
      
    # Add the table to the content.
    elements.append(table)

    # Build the PDF document.
    doc.build(elements)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="analysis_report.pdf")



# ****************************************************************

def error_404(request , exception):
     return (request , 'analysis/404.html')



def error_500(request ):
     return (request , 'analysis/500.html')

def error_400(request  ,exception):
     return (request , 'analysis/400.html')

