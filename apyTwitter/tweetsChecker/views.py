
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from django import forms

from .controllers.tweet import Tweet
from .controllers.filt import Filt
from .controllers.flag import Flag

from .controllers.factory import Factory

factory = Factory( [
    Flag("Primaire", ["Primaire"]),
    Flag("USA2016", ["Clinton","Obama"]),
    Flag("Sarkozy", ["sarkozy"]),
    Flag("Flag4", ["key_words"]),
], [
    Filt("Trump", ["Trump"]),
    Filt("Fillon", ["Fillon"]),
    Filt("Juppe", ["Juppe, Juppé"]),
    Filt("Sarkozy", ["Sarkozy"]),
])


def index (request):
    filts = factory.filters
    flags = factory.flags
    #tweets = factory.makeRequestWithNewFilter(Filt("US2016", ["Trump", "Hillary", "Obama"]))
    tweets = []
    template = loader.get_template('tweetsChecker/index.html')
    context = {
        'tweets' : tweets,
        'filts' : filts,
        'flags' : flags
    }
    return HttpResponse(template.render(context, request))

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

def addNewFlag(request):
    if request.method == 'POST' and request.POST['newFlagName'] and request.POST['newFlagKeyWords']:
        print(request.POST['newFlagName'])
        print(request.POST['newFlagKeyWords'].split(" "))
        factory.addFlag(request.POST['newFlagName'],request.POST['newFlagKeyWords'].split(" "))
    return redirect("index")

def addNewFilter(request):
    if request.method == 'POST' and request.POST['newFilterName'] and request.POST['newFilterKeyWords']:
        print(request.POST['newFilterName'])
        print(request.POST['newFilterKeyWords'].split(" "))
        factory.makeRequestWithNewFilter(Filt(request.POST['newFilterName'],request.POST['newFilterKeyWords'].split(" ")))
    return redirect("index")

def deleteFilter(request, filter_name):
    factory.deleteFilter(filter_name)
    return redirect("index")

def deleteFlag(request, flag_name):
    factory.deleteFlag(flag_name)
    return redirect("index")
