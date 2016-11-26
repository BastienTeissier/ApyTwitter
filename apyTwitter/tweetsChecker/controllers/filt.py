import urllib

class Filt:
    def __init__(self, name, key_words, count = 100 ):
        '''

        :param name: nom du filtre
        :param key_words: liste des mots clés
        :param count: nombre de tweets affichés

        '''

        if not isinstance(name,str):
            raise TypeError("Le nom du filtre doit être une chaine de caractères")
        if not isinstance(key_words, list):
            raise TypeError("key_words doit être une liste")
        for words in key_words:
            if not isinstance(words,str):
                raise TypeError("key_words doit être une liste de chaines de caractères")
        if not isinstance(count, int):
            raise TypeError("Entrez un nombre entier de tweets")
        for words in key_words:
            if words.strip() == "":
                raise ValueError("Entrez des mots clés corrects")
        #if name.strip() == "":
        #    raise ValueError("Entrez un nom de filtre correct")
        if count <= 0:
            raise ValueError("Entrez un nombre de tweets positifs")
        if count > 100:
            raise ValueError("Entrez un nombre inférieur à 100")

        self._name = name
        self.count = count

        # Mets les mots clès en minuscule

        keys = []
        for word in key_words:
            keys.append(word.lower())
        self._key_words = keys

    # Créer des properties pour tous les attributs sauf count. La modification des filtres se fait par ajout de nouveaux filtres ou suppression d'existants

    @property
    def name(self):
        return self._name

    @property
    def clean_name(self):
        return urllib.parse.quote(self._name.replace(" ","_").replace("/",""), safe='')

    @property
    def key_words(self):
        return self._key_words

    # Méthode transformant la liste de key_words initiale en dictionnaire assimilable par l'API de Twitter
    def dico(self):
        str_key_words = ""
        for words in self._key_words:
            if str_key_words == "":
                str_key_words = words
            else:
                str_key_words += '+' + words
        return {
            'q': str_key_words,
            'count' : self.count
        }

if __name__ == "__main__":
    filt1=Filt("Politics",["Trump","Hillary"],100)
    print(filt1.name)
    print(filt1.count)
    print(filt1.key_words)
    print(filt1.dico())
