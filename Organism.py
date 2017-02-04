
class Organism:

    def __init__(self, is_alive,color = None):
        """
        Constructeur de Organism
        :param is_alive: boolean qui indique si la cellule est vivant ou morte
        """
        self._is_alive = is_alive
        self._neigh = 0
        self._color = color

    def add_neigh(self):
        """ajouter un voisin a la cellule"""
        self._neigh += 1

    def reset_neigh(self):
        """reinitialiser le conteur de voisin"""
        self._neigh = 0

    def get_neigh(self):
        """
        :return: nombre de voisin
        """
        return self._neigh

    def get_display(self):
        """
        :return: la facon dont la cellule sera affiche lors de l'exectution
        """
        if self._is_alive:
            return self._color
        else:
            return "."

    def is_alive(self):
        """si la cellule est en vie"""
        return self._is_alive

    def die(self):
        """
        'tuer' la cellule.  Une cellule morte restera une instance de Green,Blue ou Rouge, mais sera
        affiche comme etant morte jusqu'a ce quelle renaisse
        """
        self._is_alive = False

