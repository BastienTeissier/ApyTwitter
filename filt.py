class Filt:
    def __init__( self, name, key_words, count = 100 ):
        self._name = name
        self._key_words = key_words #key_words est une liste de key words
        self._count = count

    @property
    def name(self):
        return self._name

    @property
    def key_words(self):
        return self._key_words

    @property
    def count(self):
        return self._count

    def dico(self):
        str_key_words = ""
        dico = {}
        for words in self.key_words:
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
    filt1 = Filt("Politics", ["Trump", "Hillary"], 100)
    print(filt1.name)
    print(filt1.count)
    print(filt1.key_words)
    print(print(filt1.dico()))





