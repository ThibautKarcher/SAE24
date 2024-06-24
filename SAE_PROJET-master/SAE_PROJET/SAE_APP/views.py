from django.shortcuts import render, HttpResponseRedirect
from .forms import DonneeForm
from . import models


def ajout(request):
    if request.method == "POST":
        form = DonneeForm(request)
        return render(request, "APP/ajout.html",{"form" : form})
    else :
        form = DonneeForm()
        return render(request, "APP/ajout.html", {"form" : form})

def traitement(request):
    lform = DonneeForm(request.POST)
    if lform.is_valid():
        donnee = lform.save()
        return HttpResponseRedirect("/SAE_APP/APP/accueil")
    else :
        return render(request, "APP/ajout.html", {"form": lform})


def accueil(request):
    liste = list(models.Donnee.objects.all())
    return render(request,"APP/accueil.html", {"liste" : liste})

def affiche(request, id):
    donnee = models.Donnee.objects.get(pk=id)
    return render(request, "APP/affiche.html", {"donnee": donnee})

def update(request, id):
    donnee = models.Donnee.objects.get(pk=id)
    form = DonneeForm(donnee.__dict__)
    return render(request, "APP/ajout.html", {"form": form, "id" : id})

def updatetraitement(request, id):
    lform = DonneeForm(request.POST)
    if lform.is_valid():
        donnee = lform.save(commit=False)
        donnee.id = id
        donnee.save()
        return HttpResponseRedirect("/SAE_APP/APP/accueil")
    else :
        return render(request, "APP/ajout.html", {"form" : lform})

def delete(request, id):
    donnee = models.Donnee.objects.get(pk=id)
    donnee.delete()
    return HttpResponseRedirect("/SAE_APP/APP/accueil")

