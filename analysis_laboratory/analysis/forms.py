from django.forms import ModelForm
from .models import ProductEngrais,Laborantins


class ProductFomrs(ModelForm):
    class Meta:
        model =ProductEngrais
        fields='__all__'


class LaboratinsFomrs(ModelForm):
    class Meta:
        model =Laborantins
        fields='__all__'
        
    
   

    