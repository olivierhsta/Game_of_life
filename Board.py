


class Board:

    HEIGHT_BOARD = 10  # valeur de 10 par defaut
    WIDTH_BOARD = 10  # valeur de 10 par defaut

    def __init__(self, dict_cell, width, height):
        """
        constructeur de Board

        :param dict_cell: dictionaire contenant les positions des cellules vivantes
        :param width: largeur de la grille
        :param height: hauteur de la grille
        """
        self._dict_cell = dict_cell
        self.WIDTH_BOARD = width
        self.HEIGHT_BOARD = height
        self._string_board = ''

    def __str__(self):
        """
        fonction toString de Board

        :return: string a afficher lorsqu'on print une instance de Board
        """
        for i in range(self.HEIGHT_BOARD):
            for j in range(self.WIDTH_BOARD):
                try:
                    self._string_board += ' ' + self._dict_cell[j+(i*self.WIDTH_BOARD)].get_color() + ' '
                except KeyError:
                    self._string_board += " . "
            self._string_board += "\n"
        return self._string_board

