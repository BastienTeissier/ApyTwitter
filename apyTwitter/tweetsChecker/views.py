
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from django import forms

from .controllers.tweet import Tweet
from .controllers.filt import Filt
from .controllers.flag import Flag

from .controllers.factory import Factory

# Instanciation de la factory qui sera manipulée par la vue
factory = Factory()

# Page d'accueil de l'application web, aucun tweet n'est chargé
def index (request):
    '''
    On récupère les listes de filtres/flags depuis notre factory
    Ces listes proviennent à priori de la base de donnée
    '''
    filts = factory.filters
    flags = factory.flags
    # Les tweets sont instanciés à la liste vide
    tweets = []
    template = loader.get_template('tweetsChecker/index.html')
    context = {
        'tweets' : tweets,
        'filts' : filts,
        'flags' : flags
    }
    return HttpResponse(template.render(context, request))

# Controller appelé à chaque fois qu'un filtre est rechargé (on renouvelle les tweets)
def reloadFilter(request, filter_name):
    print(filter_name)
    filts = factory.filters
    flags = factory.flags
    tweets = factory.makeRequestWithExistingFilter(filter_name)
    template = loader.get_template('tweetsChecker/index.html')
    context = {
        'tweets' : tweets,
        'filts' : filts,
        'flags' : flags
    }
    return HttpResponse(template.render(context, request))

# Controller utilisé pour l'ajout d'un nouveau flag, renvoie à la page de base
def addNewFlag(request):
    if request.method == 'POST' and request.POST['newFlagName'] and request.POST['newFlagKeyWords']:
        print(request.POST['newFlagName'])
        print(request.POST['newFlagKeyWords'].split(" "))
        factory.addFlag(request.POST['newFlagName'],request.POST['newFlagKeyWords'].split(" "))
    return redirect("index")

# Controlle utilise pour rajouter un nouveau filtre, renvoie la page charger avec le nouveau filtre
def addNewFilter(request):
    if request.method == 'POST' and request.POST['newFilterName'] and request.POST['newFilterKeyWords']:
        print(request.POST['newFilterName'])
        print(request.POST['newFilterKeyWords'].split(" "))
        ##
        ## A CORRIGER
        ##
        factory.makeRequestWithNewFilter(Filt(request.POST['newFilterName'],request.POST['newFilterKeyWords'].split(" ")))
    return redirect("index")

def deleteFilter(request, filter_name):
    factory.deleteFilter(filter_name)
    return redirect("index")

def deleteFlag(request, flag_name):
    factory.deleteFlag(flag_name)
    return redirect("index")

# Controller utilisé pour la recherche sans filtre persistant
def search(request):
    if request.method == 'POST' and request.POST['keyWords']:
        filts = factory.filters
        flags = factory.flags
        tweets = factory.makeRequestWithNewFilter(Filt("",request.POST['keyWords'].split(" ")))
        print(tweets)
        template = loader.get_template('tweetsChecker/index.html')
        context = {
            'tweets' : tweets,
            'filts' : filts,
            'flags' : flags
        }
        return HttpResponse(template.render(context, request))
