class Flag:
    def __init__(self, name, key_words):
        '''

        :param name: nom du flag
        :param key_words: liste des mots clés

        '''

        if not isinstance(name,str):
            raise TypeError("Le nom du flag doit être une chaine de caractères")
        if not isinstance(key_words,list):
            raise TypeError("key_words doit être une liste")
        for word in key_words:
            if not isinstance(word,str):
                raise TypeError("Les mots clés doivent être des chaines de caractères")
        if name.strip() == "":
            raise ValueError("Entrez un nom de flag correct")
        for word in key_words:
            if word.strip() == "":
                raise ValueError("Entrez des mots clés corrects")

        self._name = name

        keys = []
        for word in key_words:
            keys.append(word.lower())
        self._key_words = keys

    @property
    def name(self):
        return self._name

    @property
    def key_words(self):
        return self._key_words

if __name__ == "__main__":
    flag1 = Flag("Politics", ["Obama"])
    print(flag1.name)
    print(flag1.key_words)