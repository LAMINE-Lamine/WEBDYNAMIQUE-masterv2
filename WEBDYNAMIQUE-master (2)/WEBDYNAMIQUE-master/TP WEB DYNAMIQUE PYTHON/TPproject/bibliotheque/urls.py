from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('ajout2/', views.ajout2),
    path('traitementupdate2/<int:id>/', views.traitementupdate2),
    path('delete2/<int:id>', views.delete2),
    path('traitement2/', views.traitement2),
    path('update2/<int:id>', views.update2),
    path('traitement3/<int:id>/', views.traitement3),
    path('traitementupdate3/<int:id>/', views.traitementupdate3),
    path('ajout3/<int:id>/', views.ajout3),
]
