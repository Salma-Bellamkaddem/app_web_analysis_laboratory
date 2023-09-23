from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProductFomrs(ModelForm):
    class Meta:
        model =ProductEngrais
        fields='__all__'



class EchantillonFomrs(ModelForm):
    class Meta:
        model =Echantillon
        fields='__all__'

class LaboratinsFomrs(ModelForm):
    class Meta:
        model =Laborantins
        fields='__all__'
        exclude = ['user']



class AnalyseFomrs(ModelForm):
    class Meta:
        model =ProductAnalyse
        
        fields=["num", "laborantins", "location", "product_name","type_produit","type_analyse","resultat","status"]
        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }





        
    
   

    