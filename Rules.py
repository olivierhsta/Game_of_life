
from Organism import Organism

class Rules:

    def read_rules(self):
        """
        lire le fichier texte contenant le nombre de voisin necessaire pour
        qu'une cellule d'une couleur x naisse/survive/meurt

        :return: un dictionaire des regles pour chacune des couleurs
        """
        dict_rules = {}                                     # dictionnaire contenant les valeurs de naissance, survie et mort des cellules
        fr = open("rules.txt", 'r')
        for line in fr:
            line = line.strip()                             # retirer le \n final
            color, rules = line.split(':')
            list_rules = rules.split(',')
            list_rules = [int(i) for i in list_rules]
            dict_rules[color] = list_rules                  # ajouter un element {color : [list[0], list[1], ..., list[n]]}
        fr.close()
        return dict_rules


    def read_dimension(self):
        """
        lire les dimensions de la grille dans le fichier texte

        :return: les dimensions de la grille
        """
        fr = open("config.txt", 'r')
        line = fr.readline()
        line = line.strip()                             # retirer le \n final
        x, y = line.split(',')
        x, y = int(x), int(y)
        fr.close()
        return x, y

    def read_config(self, dict_rules, width_board):
        """
        lire le fichier texte contenant la configuration des cellules vivantes dans la grille

        :param dict_rules: un dictionaire des regles pour chacune des couleurs
        :return: un dictionaire contenant la position des cellules vivantes
        """

        dict_position_cell = {}                             # dictionaire contenant les elements de la grille
        fr = open("config.txt", 'r')
        fr.readline()
        for line in fr:
            line = line.strip()                             # retirer le \n final
            list_position = line.split(',')
            org = Organism(True, int(list_position[1]), int(list_position[2]), dict_rules.get('R')[0], dict_rules.get('R')[-1], list_position[0])
            dict_position_cell[(int(list_position[1]))+(int(list_position[2])*width_board)] = org
        fr.close()
        return dict_position_cell
