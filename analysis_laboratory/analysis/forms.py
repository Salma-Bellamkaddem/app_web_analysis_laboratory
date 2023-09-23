from django.forms import ModelForm
from .models import ProductEngrais,Laborantins,ProductAnalyse,Echantillon


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



class AnalyseFomrs(ModelForm):
    class Meta:
        model =ProductAnalyse
        
        fields='__all__'





        
    
   

    