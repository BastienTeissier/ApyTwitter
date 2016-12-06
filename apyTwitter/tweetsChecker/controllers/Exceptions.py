class Mon_exception(Exception):
    def __init__(self,raison, code = 500):
        self.raison = raison
        self.code = code

    def __str__(self):
        return self.raison
