from ..controllers.comTwitter import ComTwitter as cT
from ..controllers.flagManager import FlagManager as fM
from ..controllers.filt import Filt
from ..controllers.flag import Flag
from ..controllers.tweet import Tweet
from ..models import FlagModel, FiltModel


class Factory:
    cTwitter = cT()

    def __init__(self, flags=[], filters=[]):
        list_flags = FlagModel.get_saved_flags()
        flags = flags + list_flags
        list_filters = FiltModel.get_saved_filt()
        filters = filters + list_filters
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
        if fil.name!="":
            self.addFilter(fil)
        r = Factory.cTwitter.makeGetRequest("https://api.twitter.com/1.1/search/tweets.json", fil.dico())
        self.flagManager.putFlags(r)
        if fil.name:
            self.filters += [fil]
        return r

    def addFlag(self, flag):
        model = FlagModel()
        model.to_model(flag)
        model.save()
        self.flags.append(flag)
        self.flagManager.setFlags(self.flags)

    def addFlag(self, name, key_words):
        flag = Flag(name, key_words)
        model = FlagModel()
        model.to_model(flag)
        model.save()
        self.flags.append(Flag(name, key_words))
        self.flagManager.setFlags(self.flags)

    def deleteFlag(self, flag_name):
        for flag in self.flags:
            if flag.clean_name == flag_name:
                self.flags.remove(flag)
                self.flagManager.setFlags(self.flags)
                FlagModel.delete_flag(flag.name)
                break

    def addFilter(self, fil):
        model = FiltModel()
        model.to_model(fil)
        model.save()
        self.filters.append(fil)

    def deleteFilter(self, filter_name):
        for fil in self.filters:
            if fil.clean_name == filter_name:
                self.filters.remove(fil)
                FiltModel.delete_filt(fil.name)
                break


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
