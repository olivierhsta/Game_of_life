from Organism import Organism

class Green(Organism):
    DEATH = 2
    BIRTH = 2
    SURVIE = 1
    COLOR = 'G'

    def __init__(self, x, y):
        super().__init__(True, x, y, self.BIRTH, self.DEATH, self.COLOR)