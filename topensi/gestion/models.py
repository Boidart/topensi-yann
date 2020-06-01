from django.db import models
from month.models import MonthField
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Partenaire(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
class Type(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Etat(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class InfoVente(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    typ = models.ForeignKey(Type, on_delete=models.CASCADE)
    Pachat = models.FloatField(null=True)
    Pvente = models.FloatField(null=True)
    recurrent = models.FloatField(null=True)
    marge = models.FloatField(null=True)


class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    typ = models.ForeignKey(Type, on_delete=models.CASCADE)
    etat = models.ForeignKey(Etat, on_delete=models.CASCADE)
    facture = models.BooleanField()
    dateCreation = MonthField()
    dateCloture = MonthField()
    dateInstallation = models.DateField(null=True)

class Droit(models.Model):
    utilisateur =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="userdroit")
    autorisation = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autorisation")
    
    def __unicode__(self):
        return unicode(self.month) 