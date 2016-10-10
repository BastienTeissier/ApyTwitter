class Factory:
    flagManager = FlagManager()
    comTwitter = ComTwitter()

    def __init__(self, flags, filters):
        self.flags = flags
        self.filters = filters

    # Ajout des nouveaux flags/filters dans mainRest

    def makeRequestWithExistingFilter(self, filter_name):

    def makeRequestWithNewFilter(self, filter):
