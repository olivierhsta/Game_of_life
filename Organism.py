

class Organism:

    def __init__(self, is_alive, x, y, birth=None, death=None, color=None):
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
        self._is_alive = is_alive
        self._neigh = 0

    def add_neigh(self):
        self._neigh += 1

    def get_neigh(self):
        return self._neigh

    def get_color(self):
        if self._is_alive:
            return ' ' + self._color + ' '
        else:
            return " . "

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_is_alive(self):
        return self._is_alive
