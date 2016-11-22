from ..controllers.comTwitter import ComTwitter as cT
from ..controllers.flagManager import FlagManager as fM
from ..controllers.filt import Filt
from ..controllers.flag import Flag
from ..controllers.tweet import Tweet

class Factory:
    cTwitter = cT()

    def __init__(self, flags=[], filters=[]):
        self.flags = flags
        self.flagManager = fM(flags)
        self.filters = filters

    # Ajout des nouveaux flags/filters dans mainRest

    def makeRequestWithExistingFilter(self, filter_name, count=0):
        r = []
        for fil in self.filters:
            if fil.name == filter_name:
                if count ==0 :
                    count = fil.count
                else:
                    fil.count = count
                r = Factory.cTwitter.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', fil.dico())
                break
        self.flagManager.putFlags(r)
        return r

    def makeRequestWithNewFilter(self, fil):
        print(fil.dico())
        r = Factory.cTwitter.makeGetRequest("https://api.twitter.com/1.1/search/tweets.json", fil.dico())
        self.flagManager.putFlags(r)
        if fil.name:
            self.filters += [fil]
        return r

    def addFlag(self, flag):
        self.flags.append(flag)
        self.flagManager.setFlags(self.flags)

    def addFlag(self, name, key_words):
        self.flags.append(Flag(name, key_words))
        self.flagManager.setFlags(self.flags)
        print("Coucou")
        for flag in self.flagManager.flags:
            print(flag.name)

    def deleteFlag(self, flag):
        self.flags.remove(flag)
        self.flagManager.setFlags(self.flags)

    def addFilter(self, fil):
        self.filters.append(fil)

    def deleteFilter(self, fil):
        self.filters.remove(fil)


if __name__ == "__main__":
    filter1 = Filt("filtre1", ["Trump"], 1000)
    flag1 = Flag("US2016", ['Trump', 'Hillary'])
    fact = Factory([flag1], [filter1])
    tweets = fact.makeRequestWithExistingFilter("filtre1")
    print(tweets)
    for tweet in tweets:
        print("============================================")
        print(tweet.text)
        print(tweet.hashtags)
        print(tweet.etiquettes)
        print("============================================")
