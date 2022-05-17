from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClasseForm
from .forms import ArmeForm
from .forms import Arme_ajoutForm

from . import  models
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = ClasseForm(request)
        if form.is_valid():
            classe = form.save()
            return HttpResponseRedirect("/bibliotheque/")
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = ClasseForm()
        return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    cform = ClasseForm(request.POST)
    if cform.is_valid():
        classe = cform.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request,"bibliotheque/ajout.html",{"form": cform})


def home(request):
    liste = list(models.Classe.objects.all())
    return render(request, 'bibliotheque/home.html', {'liste': liste})

def affiche(request, id):
    classe = models.Classe.objects.get(pk=id)
    liste2=list(models.Arme.objects.filter(classe_id=id))
    return render(request,"bibliotheque/affiche.html",{"classe" : classe,"liste2":liste2})

def delete(request, id):
    classe = models.Classe.objects.get(pk=id)
    classe.delete()
    return HttpResponseRedirect("/bibliotheque/")

def update(request, id):
    classe= models.Classe.objects.get(pk=id)
    cform = ClasseForm(classe.dico())
    return render(request, "bibliotheque/update.html", {"form": cform,"id": id})

def traitementupdate(request, id):
    cform = ClasseForm(request.POST)
    if cform.is_valid():
        classe = cform.save(commit=False)
        classe.id = id
        classe.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": cform, "id": id})




def ajout2(request):
    if request.method == "POST":

        form = ArmeForm(request)
        if form.is_valid():
            arme = form.save()
            return render(request,"bibliotheque/ajout2.html",{"arme" : arme})

        else:
            return render(request,"bibliotheque/ajout2.html",{"form": form})
    else :
        form = ArmeForm()
        return render(request,"bibliotheque/ajout2.html",{"form" : form})

def traitement2(request):
    mform = ArmeForm(request.POST)
    if mform.is_valid():
        arme = mform.save()
        return render(request,"bibliotheque/affiche.html",{"arme" : arme})
    else:
        return render(request,"bibliotheque/ajout2.html",{"form": mform})


def delete2(request, id):
    arme = models.Arme.objects.get(pk=id)
    arme.delete()
    return HttpResponseRedirect("/bibliotheque/affiche/" + str(arme.classe_id) + '/')

def update2(request, id):
    arme = models.Arme.objects.get(pk=id)
    mform = ArmeForm(arme.dico())
    return render(request, "bibliotheque/update2.html", {"form": mform,'id':id})

def traitementupdate2(request, id):
    mform = ArmeForm(request.POST)
    if mform.is_valid():
        arme = mform.save(commit=False)

        arme.id = id
        arme.save()
        return HttpResponseRedirect("/bibliotheque/affiche/" + str(arme.classe_id) + '/')
    else:
        return render(request, "bibliotheque/update2.html", {"form": mform, "id": id})

def ajout3(request, id):
    form = Arme_ajoutForm()
    return render(request, "bibliotheque/ajout3.html", {"form": form, "id": id})



def traitement3(request , id):
    aform = Arme_ajoutForm(request.POST)
    classe= models.Classe.objects.get(pk=id)
    if aform.is_valid():
        arme_ajout = aform.save(commit=False)
        arme_ajout.classe_id = id
        arme_ajout.classe = classe
        arme_ajout.save()
        return HttpResponseRedirect(f"/bibliotheque/affiche/{id}/")
    else:
        return render(request, "bibliohteque/ajout3.html", {"form": aform, "id": id})

def traitementupdate3(request, id):
        aform = ArmeForm(request.POST)
        if aform.is_valid():
            arme = aform.save(commit=False)
            arme.id = id
            arme.save()
            return HttpResponseRedirect("/bibliotheque")
        else:
            return render(request, "bibliotheque/update3.html", {"form": aform, "id": id})