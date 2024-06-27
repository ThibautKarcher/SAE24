from django.db import models



class Donnee(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    temperature = models.FloatField(max_length=100)
    id_capteur = models.ForeignKey("Capteur", on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = 'donnee'


class Capteur(models.Model):
    maison = models.CharField(max_length=100)
    piece = models.CharField(max_length=100)
    id_capteur = models.CharField(max_length=100)

    class Meta:
        db_table = 'capteur'
