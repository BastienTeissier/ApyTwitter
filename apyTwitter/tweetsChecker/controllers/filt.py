import urllib
from ..controllers.Exceptions import *
from ..controllers.config import logging

class Filt:
    def __init__(self, name, key_words, count = 100 ):
        '''

        :param name: nom du filtre
        :param key_words: liste des mots clés
        :param count: nombre de tweets affichés

        '''
        logging.info('Creation d\'un nouveau filtre')
        if not isinstance(name,str):
            logging.warning('Nom %s invalide pour nouveau filtre', name)
            raise Mon_exception("Entrez un nom de filtre correct")
        if not isinstance(key_words, list):
            logging.warning('%s n\'est pas une liste de key_words', key_words)
            raise TypeError("key_words doit être une liste")
        for words in key_words:
            if not isinstance(words,str):
                logging.warning('Le key_word %s n\'est pas au format string', words)
                raise TypeError("key_words doit être une liste de chaines de caractères")
        if not isinstance(count, int):
            logging.warning('Le count %s n\'est pas un entier', count)
            raise TypeError("Entrez un nombre entier de tweets")
        for words in key_words:
            if words.strip() == "":
                logging.warning('key_words contient une entrée vide')
                raise Mon_exception("Entrez des mots-clés corrects")

        self._name = name
        self.count = count

        # Mets les mots clès en minuscule

        keys = []
        for word in key_words:
            keys.append(word.lower())
        self._key_words = keys
        logging.info('Filtre %s créé', name)

    '''Créer des properties pour tous les attributs sauf count.
    La modification des filtres se fait par ajout de nouveaux filtres ou suppression de ceux existants'''

    @property
    def name(self):
        return self._name

    @property
    def clean_name(self):
        return self._name.replace(" ","_").replace("/","")

    @property
    def key_words(self):
        return self._key_words

    # Méthode transformant la liste de key_words initiale en dictionnaire assimilable par l'API de Twitter
    def dico(self):
        logging.info('Formatage des key_words pour l\'API')
        str_key_words = ""
        for words in self._key_words:
            if str_key_words == "":
                str_key_words = words
            else:
                str_key_words += '+' + words
        logging.debug('key_words formatés : %s', str_key_words)
        return {
            'q': str_key_words,
            'count' : self.count
        }

if __name__ == "__main__":
    try:
        filt1=Filt("Politics",["Trump","Hillary"],100)
        print(filt1.name)
    except Mon_exception as err:
        print(err.__str__())


