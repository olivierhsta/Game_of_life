from Organism import Organism

class Red(Organism):
    DEATH = 3               # meurt avec 3 voisins par defaut
    BIRTH = 3               # nait avec 3 voisins par defaut
    COLOR = 'R'

    def __init__(self, x, y):
        super().__init__(True, x, y, self.BIRTH, self.DEATH, self.COLOR)