from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ClasseForm(ModelForm):
    class Meta:
        model = models.Classe
        fields = ('titre','resume')
        labels = {
            'titre': _('Titre'),
            'resume': _('Resume'),
        }

class ArmeForm(ModelForm):

    class Meta:
        model = models.Arme
        fields = ('nom_d_arme','createur','nombre_d_exemplaire','date_creation','porte','classe','image')
        labels = {
            'nom_d_arme': _("Nom d'arme"),
            'createur': _('Createur'),
            'nombre_d_exemplaire': _("Nombre d'exemplaire"),
            'date_creation':  _("Date creation"),
            'porte': _('Porte'),


        }


class Arme_ajoutForm(ModelForm):
    class Meta:
        model = models.Arme
        fields = ('nom_d_arme', 'createur', 'nombre_d_exemplaire', 'date_creation', 'porte', 'image')
        labels = {
            'nom_d_arme': _("Nom d'arme"),
            'createur': _('Createur'),
            'nombre_d_exemplaire': _("Nombre d'exemplaire"),
            'date_creation': _("Date creation"),
            'porte': _('Porte'),
        }


