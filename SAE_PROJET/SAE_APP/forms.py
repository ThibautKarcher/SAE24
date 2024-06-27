# myapp/forms.py
from django import forms
from django.forms import ModelForm
from .models import Donnee, Capteur


class FiltrerDonneesForm(forms.Form):
    date_debut = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date Début')
    date_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date Fin')
    heure_debut = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}), label='Heure Début')
    heure_fin = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}), label='Heure Fin')
    temperature_min = forms.FloatField(required=False, label='Température Min')
    temperature_max = forms.FloatField(required=False, label='Température Max')


class UpdateCapteurForm(ModelForm):
    class Meta:
        model = Capteur
        fields = ['maison', 'piece', 'id_capteur']
        labels = {
            'maison': 'Maison',
            'piece': 'Pièce',
        }
