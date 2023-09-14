from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Laboratoire)
admin.site.register(Laborantins)
admin.site.register(Location)
admin.site.register(Echantillon)
admin.site.register(ProductEngrais)
admin.site.register(TypeProduit)
admin.site.register(TypeAnalyse)
admin.site.register(ProductAnalyse)
admin.site.register(Resultat)
admin.site.register(History)
admin.site.register(Notif)


