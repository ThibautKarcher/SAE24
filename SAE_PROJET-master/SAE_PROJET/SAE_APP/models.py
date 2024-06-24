from django.db import models

# Create your models here.



class Donnee(models.Model):
    id_capteur = models.CharField(max_length=50)
    nom_capteur = models.CharField(max_length=50)
    periode_temps = models.DateTimeField()
    valeur = models.FloatField()

    def __str__(self):
        return f"L'id du capteur est {self.id_capteur}, le nom du capteur est {self.nom_capteur}, la période de temps est {self.periode_temps}, et à pour valeur {self.valeur}"
        return chaine