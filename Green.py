from Organism import Organism


class Green(Organism):
    DEATH = 3               # meurt avec 3 voisins par defaut
    BIRTH = 2               # nait avec 2 voisins par defaut
    SURVIE = 2              # survie avec 2 voisin par defaut
    COLOR = 'G'

    def __init__(self):
        super().__init__(True, self.COLOR)

    def show_color(self):
        """
        permet d'activer le mode dans lequel les couleurs sont affiche lors de l'execution
        """
        self.COLOR = '\x1b[32m' + 'G' + '\x1b[0m'
