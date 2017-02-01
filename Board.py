
from Organism import Organism
from Red import Red
from Green import Green
from Blue import Blue

class Board:

    def __init__(self, dict_cell={}, width=10, height=10):
        """
        constructeur de Board

        :param dict_cell: dictionaire contenant les positions des cellules vivantes
        :param width: largeur de la grille
        :param height: hauteur de la grille
        """
        self._dict_cell = dict_cell
        global WIDTH_BOARD
        global HEIGHT_BOARD
        WIDTH_BOARD = width
        HEIGHT_BOARD = height
        self._list_organism = []
        for j in range(HEIGHT_BOARD):
            for i in range(WIDTH_BOARD):
                try:
                    # execute en O(n) car rechercher dans un dictionaire execute en O(1)
                    self._list_organism.append(self._dict_cell[i+(j*WIDTH_BOARD)])
                except KeyError:
                    self._list_organism.append(Organism(False, i, j))

    def find_neigh(self):
        """
        trouver le nombre de voisin vivant de chaque cellule

        :return: nada
        """

        for j in range(HEIGHT_BOARD):
            for i in range(WIDTH_BOARD):

                current = i + (j * WIDTH_BOARD)

                try:
                    if current - WIDTH_BOARD > 0 and self._list_organism[current - WIDTH_BOARD].get_is_alive():
                        # cellule au-dessus de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if self._list_organism[current + WIDTH_BOARD].get_is_alive():
                        # cellule en-dessous de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if current%WIDTH_BOARD != 0 and self._list_organism[current - 1].get_is_alive():
                        # cellule a gauche de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if current%WIDTH_BOARD != WIDTH_BOARD-1 and self._list_organism[current + 1].get_is_alive():
                        # cellule a droite de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if current - WIDTH_BOARD - 1 > 0 and self._list_organism[current - WIDTH_BOARD - 1].get_is_alive():
                        # cellule en diagonale en haut a gauche de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if current - WIDTH_BOARD + 1 > 0 and self._list_organism[current - WIDTH_BOARD + 1].get_is_alive():
                        # cellule en diagonale en haut a droite de la cellule courante
                        self._list_organism[current].add_neigh()
                        print("neigh added")
                except IndexError:
                    pass

                try:
                    if self._list_organism[current + WIDTH_BOARD - 1].get_is_alive():
                        # cellule en diagonale en bas a gauche de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError:
                    pass

                try:
                    if self._list_organism[current + WIDTH_BOARD + 1].get_is_alive():
                        # cellule en diagonale en bas a droite de la cellule courante
                        self._list_organism[current].add_neigh()
                except IndexError :
                    pass




    def turn(self):
        for j in range(HEIGHT_BOARD):
            for i in range(WIDTH_BOARD):
                current = i + (j * WIDTH_BOARD)
                if self._list_organism[current].get_neigh() == Red.BIRTH and self._list_organism[current].get_color() == " . ":
                    self._list_organism[current] = Red(i,j)
                if self._list_organism[current].get_neigh() == Blue.BIRTH and self._list_organism[current].get_color() == " . ":
                    self._list_organism[current] = Blue(i,j)
                if self._list_organism[current].get_neigh() == Green.BIRTH and self._list_organism[current].get_color() == " . ":
                    self._list_organism[current] = Green(i,j)


    def __str__(self):
        """
        fonction toString de Board

        :return: string a afficher lorsqu'on print une instance de Board
        """

        _string_board=""
        for j in range(HEIGHT_BOARD):
            for i in range(WIDTH_BOARD):
                _string_board += self._list_organism[i+(j*WIDTH_BOARD)].get_color()
            _string_board += "\n"
        return _string_board

