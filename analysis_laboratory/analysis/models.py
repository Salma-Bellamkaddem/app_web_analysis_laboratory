
from django.db import models
from django.db.models import Avg


# Create your models here.


class Laboratoire(models.Model):
    lab_name = models.CharField(max_length=255)
    lab_address = models.TextField()
    lab_contact = models.CharField(max_length=255)
    address = models.TextField()


    def __str__(self):
        return self.lab_name
   

class Laborantins(models.Model):
    lab = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=50 ,null=True)
    first_name = models.CharField(max_length=100 ,null=True)
    last_name = models.CharField(max_length=100 ,null=True)
    telephone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    address = models.TextField( )
    skills = models.CharField(max_length=200, null=True)
    date_create=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.location_name


class Echantillon(models.Model):
    code_echantillon = models.IntegerField(unique=True)
    quantite = models.FloatField()
    date_prelevement = models.DateField()
    date_reception = models.DateField()
    observation = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)   

   

    def __str__(self):
        return f" {self.code_echantillon}"
    


class ProductEngrais(models.Model):
    echantillon=models.ForeignKey(Echantillon, on_delete=models.CASCADE)  
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)   
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField()

    def __str__(self):
        return self.product_name


class TypeProduit(models.Model):
    nom_type_produit = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_type_produit
    class Meta:
        db_table = 'type_produit'


class TypeAnalyse(models.Model):
    nom_type_analyse = models.CharField(max_length=255)
  
    def __str__(self):
        return self.nom_type_analyse
    
    class Meta:
        db_table = 'type_analyse'




class ProductAnalyse(models.Model):
    num= models.CharField(max_length=50 ,null=True)
    laborantins = models.ForeignKey(Laborantins, on_delete=models.CASCADE)
    location =models.ForeignKey(Location, on_delete=models.CASCADE)
    product_name=models.ForeignKey( ProductEngrais, on_delete=models.CASCADE)
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(TypeAnalyse, on_delete=models.CASCADE)
    resultat  = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField()
  
    ENCOUR = 'encour'
    REALISE = 'realise'
    STATUS_CHOICES = [
        (ENCOUR, 'En cours'),
        (REALISE, 'Réalisé'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ENCOUR)
    
    def __str__(self):
        return f"      {self.num} "

    

class Notif(models.Model):
    laborantins = models.ForeignKey('Laborantins', on_delete=models.CASCADE)
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lue = models.BooleanField(default=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-date_creation']





class Resultat(models.Model):
    # Informations sur l'analyse
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    echantillon = models.ForeignKey(Echantillon, on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(TypeAnalyse, on_delete=models.CASCADE)
    produit_angrais = models.ForeignKey(ProductEngrais, on_delete=models.CASCADE)
    date_analyse = models.DateTimeField()
    
    # Résultats spécifiques de l'analyse
    valeur_mesuree = models.DecimalField(max_digits=10, decimal_places=2)
    unite_mesure = models.CharField(max_length=50)
    limite_detection = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Autres informations
    commentaire = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Analyse de {self.echantillon} ({self.type_analyse}) du {self.date_analyse}"
    



class History(models.Model):
    resultat_analyse = models.ForeignKey(Resultat, on_delete=models.CASCADE)
    date_modification = models.DateTimeField(auto_now_add=True)
    laborantins = models.ForeignKey('Laborantins', on_delete=models.CASCADE)
    champ_modifie = models.CharField(max_length=255)
    ancienne_valeur = models.CharField(max_length=255)
    nouvelle_valeur = models.CharField(max_length=255)

    def __str__(self):
        return f"Modifications pour {self.resultat_analyse}"

    class Meta:
        verbose_name = "Historique d'Analyse"
        verbose_name_plural = "Historiques d'Analyse"


class MoyenneAnalyse(models.Model):
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(TypeAnalyse, on_delete=models.CASCADE)
    moyenne = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.type_produit} - {self.type_analyse} - Moyenne : {self.moyenne} ({self.date})"