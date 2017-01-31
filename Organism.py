

class Organism:

    def __init__(self, birth, death, color, x, y):
        """
        constructeur de Organism

        :param birth: nombre de voisins necessaires pour que la cellule naisse
        :param death: nombre de voisin necessaires pour que la cellule meurt
        :param color: couleur de la cellule
        :param x: position en x de la cellule
        :param y: positon en y de la cellule
        """
        self._birth = birth
        self._death = death
        self._color = color
        self._x = x
        self._y = y

    def __str__(self):
        return "---------------\nCouleur : " + self._color + "\nX : " + str(self._x) + "\nY : " + str(self._y)

    def get_color(self):
        return self._color

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y