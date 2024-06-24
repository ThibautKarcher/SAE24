from django.urls import path
from . import views


urlpatterns = [
    path('APP/ajout/', views.ajout),
    path('APP/traitement/', views.traitement),
    path('APP/accueil/', views.accueil),
    path('APP/affiche/<int:id>/', views.affiche),
    path('APP/update/<int:id>/', views.update),
    path('APP/updatetraitement/<int:id>/', views.updatetraitement),
    path('APP/delete/<int:id>/', views.delete),
]