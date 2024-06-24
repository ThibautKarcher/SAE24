from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class DonneeForm(ModelForm):
    class Meta :
        model = models.Donnee
        fields = ('id_capteur', 'nom_capteur', 'periode_temps', 'valeur')
        labels = {
            'id_capteur' : _('Id du capteur'),
            'nom_capteur' : _('Nom du capteur'),
            'periode_temps' : _('Période de temps'),
            'valeur' : _('Valeur')
        }