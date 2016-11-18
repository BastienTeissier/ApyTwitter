from django.http import HttpResponse
from django.template import loader

from .controllers.tweet import Tweet
from .controllers.filt import Filt
from .controllers.flag import Flag

from .controllers.factory import Factory

factory = Factory()

def index (request):
    filts = [
        Filt("Filtre1", ["key_words"]),
        Filt("Filtre1", ["key_words"]),
        Filt("Filtre1", ["key_words"]),
        Filt("Filtre1", ["key_words"]),
    ]
    flags = [
        Flag("Filtre1", ["key_words"]),
        Flag("Filtre1", ["key_words"]),
        Flag("Filtre1", ["key_words"]),
        Flag("Filtre1", ["key_words"]),
    ]
    tweets = factory.makeRequestWithNewFilter(Filt("US2016", ["Trump", "Hillary", "Obama"]))
    template = loader.get_template('tweetsChecker/index.html')
    context = {
        'tweets' : tweets,
        'filts' : filts,
        'flags' : flags
    }
    return HttpResponse(template.render(context, request))

def reloadIndex(request, filter_name):
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

#def addFlag(request, name, key_words):
#    factory.
