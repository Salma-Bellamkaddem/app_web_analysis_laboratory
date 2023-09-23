import django_filters
from django_filters import DateFilter, CharFilter
from django_filters import ModelChoiceFilter


from .models import *



class AnalyseFilter(django_filters.FilterSet):
    location = ModelChoiceFilter(queryset=Location.objects.all())
    product_name= ModelChoiceFilter(queryset=ProductEngrais.objects.all())
    date_created = DateFilter(field_name="date_created", lookup_expr='exact')

    class Meta:
        model = ProductAnalyse
        fields = ['location','product_name', 'date_created']
