from Organism import Organism

class Blue(Organism):
    DEATH = 1
    BIRTH = 1
    SURVIE = 1
    COLOR = 'B'

    def __init__(self, x, y):
        super().__init__(True, x, y, self.BIRTH, self.SURVIE, self.DEATH, self.COLOR)