class Nom_incorrect(Exception):
    def __init__(self):
        self.raison = "Entrez un nom de filtre correct"
    def __str__(self):
        return self.raison

class Mots_cles_incorrects(Exception):
    def __init__(self):
        self.raison = "Entrez des mots-clés corrects"
    def __str__(self):
        return self.raison

