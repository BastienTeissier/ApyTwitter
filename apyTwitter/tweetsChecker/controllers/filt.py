class Filt:
    def __init__(self, name, key_words, count = 100 ):

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
            if words == "":
                raise ValueError("Entrez des mots clés corrects")
        if name == "":
            raise ValueError("Entrez un nom de filtre correct")
        if count <= 0:
            raise ValueError("Entrez un nombre de tweets positifs")
        if count > 100:
            raise ValueError("Entrez un nombre inférieur à 100")


        self._name = name           #le nom de notre filtre
        self._key_words = key_words #la liste des key_words
        self.count = count          #le nombre de tweets affichés


    @property
    def name(self):
        return self._name

    @property
    def key_words(self):
        return self._key_words

    def dico(self):
        str_key_words = ""
        print(self._key_words)
        for words in self._key_words:
            if str_key_words == "":
                str_key_words = words
            else:
                str_key_words += '+' + words #on transforme notre liste de key words en une chaine de caractères assimilable par l'API
        dico = {
            'q': str_key_words,
            'count' : self.count
        }
        return dico

if __name__ == "__main__":
    filt1=Filt("Politics",["Trump","Hillary"],100)
    print(filt1.name)
    print(filt1.count)
    print(filt1.key_words)
    print(filt1.dico())
