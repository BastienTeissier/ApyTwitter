import urllib
from ..controllers.Exceptions import *

class Flag:
    def __init__(self, name, key_words):
        '''

        :param name: nom du flag
        :param key_words: liste des mots clés

        '''

        if not isinstance(name,str):
            raise Mon_exception("Entrez un nom de flag correct")
        if not isinstance(key_words,list):
            raise TypeError("key_words doit être une liste")
        for word in key_words:
            if not isinstance(word,str):
                raise Mon_exception("Entrez des mots-clés corrects")
        if name.strip() == "":
            raise Mon_exception("Entrez un nom de flag correct")
        for word in key_words:
            if word.strip() == "":
                raise Mon_exception("Entrez des mots_clés corrects")

        self._name = name

        # Mets les mots clés en minuscule

        keys = []
        for word in key_words:
            keys.append(word.lower())
        self._key_words = keys

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
