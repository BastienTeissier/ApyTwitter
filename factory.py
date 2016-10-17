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
        for filt in self.filters:
            if filt.name == filter_name:
                r = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', filt)
                break
        fM.putFlags(r)
        return r

    #def makeRequestWithNewFilter(self, filter):

if __name__ == "__main__":
    factory = Factory([fa.Flag("sexe", ["bite", "chibre"])], [fi.Filt("Trump", ["Trump", "Pussy"])])
