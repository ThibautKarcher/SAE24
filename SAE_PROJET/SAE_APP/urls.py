from . import models, views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('test/', views.test),
    path('donnees/filtrer/', views.filtrer_donnees, name='filtrer_donnees'),
    path('APP/update/<int:id>/', views.update_capteur, name='update_capteur'),
    path('APP/update_process/<int:id>/', views.update_capteur_process, name='update_capteur'),
    path('APP/delete/<int:id>/', views.delete_capteur, name='delete_capteur'),
    path('export/capteur/', views.export_capteur_csv, name='export_capteur_csv'),
    path('export/donnee/', views.export_donnee_csv, name='export_donnee_csv'),
]
