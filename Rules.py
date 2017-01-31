
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
        fr = open("config.txt", 'r')
        for line in fr:
            line = line.strip()  # retirer le \n final
            x,y = line.split(',')
            x,y = int(x),int(y)
            break
        fr.close()
        return x,y

    def read_config(self, dict_rules, width_board):
        """
        lire le fichier texte contenant la configuration des cellules vivantes dans la grille

        :param dict_rules: un dictionaire des regles pour chacune des couleurs
        :return: un dictionaire contenant la position des cellules vivantes
        """
        dict_position_cell = {}                             # liste contenant les elements de la grille
        first_line = True
        fr = open("config.txt", 'r')
        for line in fr:
            line = line.strip()                             # retirer le \n final
            list_position = line.split(',')
            if first_line:
                first_line = False
            else:
                dict_position_cell[(int(list_position[1]))+(int(list_position[2])*width_board)] = \
                    (Organism(dict_rules.get('R')[0], dict_rules.get('R')[-1], list_position[0], int(list_position[1]), int(list_position[2])))
        fr.close()
        return dict_position_cell
