import urllib
from ..controllers.Exceptions import *
from ..controllers.config import logging

class Flag:
    def __init__(self, name, key_words):
        '''

        :param name: nom du flag
        :param key_words: liste des mots clés

        '''
        logging.info('Création d\'un nouveau flag')
        if not isinstance(name,str):
            logging.warning('Nom %s invalide pour nouveau flag', name)
            raise Mon_exception("Entrez un nom de flag correct")
        if not isinstance(key_words,list):
            logging.warning('%s n\'est pas une liste de key_words', key_words)
            raise TypeError("key_words doit être une liste")
        for word in key_words:
            if not isinstance(word,str):
                logging.warning('Le key_word %s n\'est pas au format string', words)
                raise Mon_exception("Entrez des mots-clés corrects")
        if name.strip() == "":
            logging.warning('Nom de flag vide')
            raise Mon_exception("Entrez un nom de flag correct")
        for word in key_words:
            if word.strip() == "":
                logging.warning('key_words contient une entrée vide')
                raise Mon_exception("Entrez des mots_clés corrects")

        self._name = name

        # Mets les mots clés en minuscule

        keys = []
        for word in key_words:
            keys.append(word.lower())
        self._key_words = keys
        logging.info('Nouveau Flag %s créé', name)

    '''Créer des properties pour tous les attributs.
    La modification de flag se fait par ajout de nouveaux flags ou suppression d'existants.'''

    @property
    def name(self):
        return self._name

    @property
    def clean_name(self):
        return self._name.replace(" ","_").replace("/","")

    @property
    def key_words(self):
        return self._key_words

if __name__ == "__main__":
    flag1 = Flag("Politics", ["Obama"])
    print(flag1.name)
    print(flag1.key_words)
