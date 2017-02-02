from Organism import Organism


class Green(Organism):
    DEATH = 2
    BIRTH = 2
    SURVIE = 1
    COLOR = 'G'

    def __init__(self, x, y):
        super().__init__(True, x, y, self.BIRTH, self.SURVIE, self.DEATH, self.COLOR)

    def show_color(self):
        self.COLOR = '\x1b[32m' + 'G' + '\x1b[0m'
