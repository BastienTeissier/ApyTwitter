from ..controllers.flag import Flag
from ..controllers.tweet import Tweet
from ..controllers.config import logging

class FlagManager:
    def __init__(self, flags):
        self.flags = flags
        logging.info('Nouveau flagManager créé pour les flags %s', [flag.name for flag in flags])

    def putFlags(self, tweets):
        '''Ajoute le flag aux Tweets contenant tous les key-words d'un flag'''
        logging.info('Ajout des flags %s', [flag.name for flag in self.flags])
        for current_flag in self.flags:
            for current_tweet in tweets:
                if all(key_word in current_tweet.text.lower() for key_word in current_flag.key_words):
                    current_tweet.etiquettes.append(current_flag.name)
        logging.info('Flags ajoutés')

    def setFlags(self, flags):
        self.flags = flags
        logging.info('FlagManager nouvelle liste de flags %s', [flag.name for flag in self.flags])

if __name__ == "__main__":
    tweet1 = Tweet("Hello, I am Donald #Hi", "Donald", "yesterday", "New York", "Toto", 150)
    tweet2 = Tweet("Hello, I am John #6", "John", "today", "New York", "Toto", 150)
    tweets = [tweet1, tweet2]

    flag1 = Flag("Flag1", ["#hi"])
    flags = [flag1]

    Manager = FlagManager(flags)
    Manager.putFlags(tweets)
