import comTwitter as cT
import flagManager as fM
import filt as fi
import flag as fl
import tweet as tw

class Factory:
    cTwitter = cT.ComTwitter()

    def __init__(self, flags, filters):
        self.flags = flags
        self.flagManager = fM.FlagManager(flags)
        self.filters = filters

    # Ajout des nouveaux flags/filters dans mainRest

    def makeRequestWithExistingFilter(self, filter_name):
        r = []
        for fil in self.filters:
            if fil.name == filter_name:
                print(fil)
                r = Factory.cTwitter.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', fil.dico())
                break
        self.flagManager.putFlags(r)
        return r

    def makeRequestWithNewFilter(self, fil):
        print(fil.dico())
        r = Factory.cTwitter.makeGetRequest("https://api.twitter.com/1.1/search/tweets.json", fil.dico())
        self.flagManager.putFlags(r)
        if fil.name:
            self.filters += fil
        return r

    def addFlag(self, flag):
        self.flags.append(flag)
        self.flagManager.setFlags(self.flags)

    def addFlag(self, name, key_words):
        self.flags.append(fl.Flag(name, key_words))
        self.flagManager.setFlags(self.flags)

    def deleteFlag(self, flag):
        self.flags.remove(flag)
        self.flagManager.setFlags(self.flags)

    def addFilter(self, fil):
        self.filters.append(fil)

    def deleteFilter(self, fil):
        self.filters.remove(fil)


if __name__ == "__main__":
    filter1 = fi.Filt("filtre1", ["Trump"], 1000)
    flag1 = fl.Flag("US2016", ['Trump', 'Hillary'])
    fact = Factory([flag1], [filter1])
    tweets = fact.makeRequestWithExistingFilter("filtre1")
    print(tweets)
    for tweet in tweets:
        print("============================================")
        print(tweet.text)
        print(tweet.hashtags)
        print(tweet.etiquettes)
        print("============================================")
