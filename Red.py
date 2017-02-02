from Organism import Organism

class Red(Organism):
    DEATH = 3               # meurt avec 3 voisins par defaut
    BIRTH = 3               # nait avec 3 voisins par defaut
    SURVIE = 1
    COLOR = 'R'

    def __init__(self, x, y):
        super().__init__(True, x, y, self.BIRTH, self.SURVIE, self.DEATH, self.COLOR)

    def show_color(self):
        self.COLOR = '\x1b[31m' + 'R' + '\x1b[0m'