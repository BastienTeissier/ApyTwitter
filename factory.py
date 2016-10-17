import comTwitter as cT
import flagManager as fM
import filt as fi
import flag as fl
import tweet as tw

class Factory:
    comTwitter = cT.ComTwitter()

    def __init__(self, flags, filters):
        self.flags = flags
        self.flagManager = fM.FlagManager(flags)
        self.filters = filters

    # Ajout des nouveaux flags/filters dans mainRest

    def makeRequestWithExistingFilter(self, filter_name):
        r = []
        for fil in self.filters:
            if fil.name == filter_name:
                r = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', fil)
                break
        fM.putFlags(r)
        return r

    def makeRequestWithNewFilter(self, fil):
        r = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', fil)
        fM.putFlags(r)
        if fil.name:
            self.filters += fil
        return r


if __name__ == "__main__":
