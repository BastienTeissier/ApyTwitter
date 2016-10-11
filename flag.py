class Flag:
    def __init__(self, name, key_words):
        self.name = name
        keys = []
        for word in key_words:
            keys.append(word.lower())
        self.key_words = keys