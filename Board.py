from Blue import Blue
from Green import Green
from Organism import Organism
from Red import Red


class Board:

    def __init__(self, dict_cell={}, width=10, height=10):
        """
        constructeur de Board

        :param dict_cell: dictionaire contenant les positions des cellules vivantes
        :param width: largeur de la grille
        :param height: hauteur de la grille
        """
        self._dict_cell = dict_cell
        self.WIDTH_BOARD = width
        self.HEIGHT_BOARD = height
        self._list_organism = []
        for j in range(self.HEIGHT_BOARD):
            for i in range(self.WIDTH_BOARD):
                try:
                    # execute en O(n) car rechercher dans un dictionaire execute en O(1)
                    self._list_organism.append(self._dict_cell[i+(j*self.WIDTH_BOARD)])
                except KeyError:
                    self._list_organism.append(Organism(False))

    def find_neigh(self):
        """
        trouver le nombre de voisin vivant de chaque cellule

        """

        for j in range(self.HEIGHT_BOARD):
            for i in range(self.WIDTH_BOARD):

                current = i + (j * self.WIDTH_BOARD)

                if self._list_organism[current].is_alive():
                    # chaque cellule vivante ajoute 1 au compteur de voisins des cellules qu'elle touche
                    if current - self.WIDTH_BOARD > 0:
                        # cellule au-dessus de la cellule courante
                        self._list_organism[current - self.WIDTH_BOARD].add_neigh()
                    try:
                        self._list_organism[current + self.WIDTH_BOARD].add_neigh()
                        # cellule en-dessous de la cellule courante
                    except IndexError:
                        pass
                    if not current % self.WIDTH_BOARD == 0:
                        # toutes les cellules ne se trouvant pas sur le cote gauche de la grille entrent
                        self._list_organism[current - 1].add_neigh()
                        # cellule a gauche de la cellule courante
                        if current - self.WIDTH_BOARD > 0:
                            self._list_organism[current - self.WIDTH_BOARD - 1].add_neigh()
                            # cellule en diagonale en haut a gauche de la cellule courante
                        try:
                            self._list_organism[current + self.WIDTH_BOARD - 1].add_neigh()
                            # cellule en diagonale en bas a gauche de la cellule courante
                        except IndexError:
                            pass
                    if not current % self.WIDTH_BOARD == self.WIDTH_BOARD - 1:
                        # toutes les cellules ne se trouvant pas du cote droit de la grille entrent
                        try:
                            self._list_organism[current + 1].add_neigh()
                            # cellule a droite de la cellule courante
                            self._list_organism[current + self.WIDTH_BOARD + 1].add_neigh()
                            # cellule en diagonale en bas a droite de la cellule courante
                        except IndexError:
                            pass
                        if current - self.WIDTH_BOARD > 0:
                            self._list_organism[current - self.WIDTH_BOARD + 1].add_neigh()
                            # cellule en diagonale en haut a droite de la cellule courante
        # chaque operation a l'interieur execute en un temps constant, la boucle execute donc en O(n)

    def turn(self):
        """
        determiner si une cellule meurt ou nait en comparant sont nombre de voisin avec le
        nombre de voisins resquis pour naitre ou mourir

        """
        for j in range(self.HEIGHT_BOARD):
            for i in range(self.WIDTH_BOARD):

                current = i + (j * self.WIDTH_BOARD)
                is_alive = self._list_organism[current].is_alive()
                nb_neigh = self._list_organism[current].get_neigh()

                if not is_alive:
                    # remplacer les cellules mortes avec le bon nombre de voisins par des cellules vivantes
                    if nb_neigh == Red.BIRTH:
                        self._list_organism[current] = Red()
                    elif nb_neigh == Green.BIRTH:
                        self._list_organism[current] = Green()
                    elif nb_neigh == Blue.BIRTH:
                        self._list_organism[current] = Blue()
                else:
                    # tuer les cellules avec trop ou pas assez de voisins
                    color = self._list_organism[current].COLOR

                    if color == Red.COLOR:
                        if nb_neigh < Red.SURVIE or nb_neigh > Red.DEATH:
                            self._list_organism[current].die()
                    elif color == Green.COLOR:
                        if nb_neigh < Green.SURVIE or nb_neigh > Green.DEATH:
                            self._list_organism[current].die()
                    elif color == Blue.COLOR:
                        if nb_neigh < Blue.SURVIE or nb_neigh > Blue.DEATH:
                            self._list_organism[current].die()
                self._list_organism[current].reset_neigh()
        # la fonction execute en O(n)

    def __str__(self):
        """
        fonction toString de Board

        :return: string a afficher lorsqu'on print une instance de Board
        """

        _string_board = ""
        for j in range(self.HEIGHT_BOARD):
            for i in range(self.WIDTH_BOARD):
                _string_board += self._list_organism[i+(j*self.WIDTH_BOARD)].get_display() + ' '
            _string_board += "\n"
        return _string_board
        # execute en O(n)

