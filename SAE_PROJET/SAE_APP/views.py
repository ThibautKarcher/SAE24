from django.shortcuts import render
from .models import Capteur, Donnee
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
import csv
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime, time



def index(request):
    return render(request, 'APP/index.html')

def export_capteur_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="capteur.csv"'

    writer = csv.writer(response)
    writer.writerow(['maison', 'piece', 'id_capteur'])

    capteurs = Capteur.objects.all().values_list('maison', 'piece', 'id_capteur')
    for capteur in capteurs:
        writer.writerow(capteur)

    return response



def test(request):
    capteurs = Capteur.objects.all()
    donnees_par_capteur = {}

    for capteur in capteurs:
        donnees = Donnee.objects.filter(id_capteur=capteur).order_by('date', 'heure')
        donnees_par_capteur[capteur] = donnees

    context = {
        'donnees_par_capteur': donnees_par_capteur,
    }
    return render(request, 'APP/test.html', context)


def filtrer_donnees(request):
    form = FiltrerDonneesForm(request.GET)
    donnees_par_capteur = {}

    if form.is_valid():
        nom_capteur = form.cleaned_data.get('nom_capteur')
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        heure_debut = form.cleaned_data.get('heure_debut')
        heure_fin = form.cleaned_data.get('heure_fin')
        temperature_min = form.cleaned_data.get('temperature_min')
        temperature_max = form.cleaned_data.get('temperature_max')

        capteurs = Capteur.objects.all()

        if nom_capteur:
            capteurs = capteurs.filter(id_capteur__icontains=nom_capteur)

        for capteur in capteurs:
            donnees = Donnee.objects.filter(id_capteur=capteur)

            if date_debut:
                donnees = donnees.filter(date__gte=date_debut)
            if date_fin:
                donnees = donnees.filter(date__lte=date_fin)
            if heure_debut:
                donnees = donnees.filter(heure__gte=heure_debut)
            if heure_fin:
                donnees = donnees.filter(heure__lte=heure_fin)
            if temperature_min is not None:
                donnees = donnees.filter(temperature__gte=temperature_min)
            if temperature_max is not None:
                donnees = donnees.filter(temperature__lte=temperature_max)

            donnees = donnees.order_by('date', 'heure')
            donnees_par_capteur[capteur] = donnees

    context = {
        'donnees_par_capteur': donnees_par_capteur,
        'form': form,
    }

    return render(request, 'APP/index.html', context)


def update_capteur(request, id):
    capteur = Capteur.objects.get(id=id)
    form = UpdateCapteurForm(instance=capteur)

    return render(request, '/APP/update.html', {'form': form, 'capteur': capteur})


def update_capteur_process(request, id):
    capteur = Capteur.objects.get(id=id)
    form = UpdateCapteurForm(request.POST)

    if form.is_valid():
        capteur = form.save()
        capteur.id = id
        capteur.save()
        return HttpResponseRedirect('/test/')
    return render(request, 'APP/update.html', {'form': form, 'capteur': capteur})


def delete_capteur(request, id):
    capteur = Capteur.objects.get(id=id)
    capteur.delete()
    return HttpResponseRedirect('/test/')

def export_donnee_csv(request):
    # Créer la réponse HTTP avec le type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donnee.csv"'

    writer = csv.writer(response)
    writer.writerow(['date', 'heure', 'temperature', 'id_capteur'])

    donnees = Donnee.objects.all().values_list('date', 'heure', 'temperature', 'id_capteur_id')
    for donnee in donnees:
        writer.writerow(donnee)

    return response

def graphique_donnees(request):
    sensor_data = Donnee.objects.all()

    # Préparer les données pour le graphique
    heure = [time_to_seconds(data.heure) for data in sensor_data]
    temperature = [data.temperature for data in sensor_data]

    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(heure, temperature, marker='o')
    plt.title('Données des Capteurs')
    plt.xlabel('Temps')
    plt.ylabel('Valeur')
    plt.grid(True)

    # Sauvegarder le graphique dans un buffer en mémoire
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Retourner le graphique comme une réponse HTTP
    return HttpResponse(buffer, content_type='image/png')

def time_to_seconds(time_value):
    # Convertir datetime.time en secondes depuis minuit
    return (datetime.combine(datetime.min, time_value) - datetime.min).total_seconds()