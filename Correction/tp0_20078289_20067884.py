import math
import sys
from Blue import Blue
from Board import Board
from Green import Green
from Red import Red
from Rules import Rules


def receive_argv():
    """
    recevoir les arguments envoye au programme depuis le module d'execution
    :return: boolean 'wait' qui indique si l'option 'animation' a ete selectionne et
             l'entier 'rep' qui indique le nombre de repetition a effectuer
    """
    wait = False
    rep = 10
    try:
        arg = sys.argv[1]
        try:
            rep = int(arg)
        except ValueError:
            if arg == "animation":
                rep = math.inf
                wait = True
            elif arg == "couleur":
                Red.show_color(Red)
                Blue.show_color(Blue)
                Green.show_color(Green)
            else:
                print("\nMauvais argument : 10 repetions par defaut (appuyez sur -Enter pour continuer)\n")
                input()
    except Exception:
        rep = 0
        print("\n------------------------------------------------------------------------------\n\n"
              "Aucun arguments entrees\n\n"
              "Pour demarrer le projet pour un nombre n de repetition :\n"
              "subprocess.call([sys.executable,'tp0_20078289_20067884.py', 'n'])\n\n"
              "Pour demarrer le projet en couleur pour 10 repetitions :\n"
              "subprocess.call([sys.executable,'tp0_20078289_20067884.py', 'couleur'])\n\n"
              "Pour demarrer le projet en mode animation :\n"
              "subprocess.call([sys.executable,'tp0_20078289_20067884.py', 'animation'])\n"
              "\n------------------------------------------------------------------------------\n\n")
    return wait,rep


def assign_rules():
    """
    assigner les bonnes valeurs pour les variables de mort-survie-naissance
    a chacune des trois classes de couleur
    """
    Red.BIRTH = dict_rules.get('R')[0]
    Red.SURVIE = dict_rules.get('R')[1]
    Red.DEATH = dict_rules.get('R')[-1]

    Green.BIRTH = dict_rules.get('G')[0]
    Green.SURVIE = dict_rules.get('G')[1]
    Green.DEATH = dict_rules.get('G')[-1]

    Blue.BIRTH = dict_rules.get('B')[0]
    Blue.SURVIE = dict_rules.get('B')[1]
    Blue.DEATH = dict_rules.get('B')[-1]


def play():
    """ boucle de deroulement de la partie """
    i = 0
    while i < rep:
        # utilisation d'une boucle while plutot que for ici car on ne peut faire de range
        # jusqu'a l'infini (dans le cas de l'option 'animation') car math.inf est un float
        print(board)
        board.find_neigh()
        board.turn()
        i += 1
        if wait:
            input()
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

wait,rep = receive_argv()

rules = Rules()
dict_rules = Rules.read_rules(rules)
assign_rules()

width_board, height_board = Rules.read_dimension(rules)

dict_position_cell = Rules.read_config(rules, width_board)

board = Board(dict_position_cell, width_board, height_board)

play()


#-------------- RAPPORT DE CORRECTION ------------------------------------------
"""
Code de bonne qualité en général, mais trop de commentaires. Comportement
presque correct pour les tests avec règles complexes, mais queulques différences
probablement due à une application fautive des règles. Sortie avec trop
d'espaces, et on ne voulait que l'état final, sans les états intermédiaires.

Note: 61/100
    Tests: 28/60
    Respect du format de sortie: 5/10
    Qualité du code: 28/30


Voici le détail des tests:

test0: 6/10
Votre sortie:
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  R  .  .  .  .  .  .  .  . 
 .  .  .  .  .  .  .  R  R  .  .  .  .  .  . 
 .  .  .  .  .  .  R  R  R  .  .  .  .  .  . 
 .  .  .  .  .  .  R  R  .  .  .  .  .  .  . 
 .  R  R  .  .  .  R  R  .  .  .  .  .  .  . 
 R  .  B  .  .  .  R  R  .  .  .  .  .  .  . 
 R  .  .  .  .  .  R  .  .  .  .  .  .  .  . 
 R  R  .  R  G  B  R  .  .  .  .  .  .  .  . 
 .  R  .  .  .  .  R  .  .  .  .  .  .  .  . 
 .  R  .  .  .  .  R  .  .  .  .  R  .  R  . 
 .  .  R  .  .  .  R  .  .  .  R  .  .  R  . 
 .  .  .  R  R  R  B  .  .  .  .  R  .  G  . 

La réponse:
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . . . R . . . . . . . 
. . . . . . . . R . . . . . . 
. . . . . . . . . . . . . . . 
. . . . . R . . . . . . . . . 
. R R . . R . . R . . . . . . 
R . B . . R . . . . . . . . . 
R . R R R . . . . . . . . . . 
R R R . G . R R . . . . . . . 
. R . . R . R R . . . . . . . 
. R R . . R R R . . . . R . . 
. . R R R . R R . . R R . R R 
. . . R R R B . . . . . R . . 

test1: 4/10
Votre sortie:
 .  .  B  B  G  B  .  G  R  .  R  .  .  B  . 
 .  G  G  R  .  G  G  R  .  R  .  .  .  R  . 
 .  R  G  .  .  .  G  B  R  .  .  .  .  .  B 
 .  .  .  .  .  .  B  B  B  G  R  R  R  .  G 
 .  .  R  .  .  .  G  .  .  R  .  .  R  G  . 
 B  G  G  R  R  G  B  B  G  .  .  .  G  G  B 
 B  B  .  .  B  R  G  .  .  .  .  .  .  R  B 
 G  R  R  B  .  G  R  .  R  G  G  R  R  R  . 
 G  .  .  G  B  G  .  .  R  .  .  G  G  G  . 
 G  R  .  G  R  G  .  R  G  .  .  G  .  G  . 
 B  B  .  .  .  R  .  G  B  .  B  R  .  R  . 
 R  .  .  .  .  .  R  .  .  .  B  R  .  R  B 
 .  R  .  .  .  .  G  .  .  .  .  B  .  G  B 
 R  .  .  .  .  .  .  G  .  B  .  B  G  R  B 
 B  G  B  B  .  .  .  B  G  .  .  .  .  G  B 

La réponse:
. . . . . B B R . . . G G . B 
G R G G G G G . . . G G R . G 
G . . R B . . R . . G G R R G 
. . . . B . . B . R . B . G . 
. . . R . . . . B R R R B B . 
R . . . B . . . . . . G B . . 
B G . . R R B . . B . R G . . 
B R . . . R . . . B . R G . . 
. . R . . . R B . B . . . R . 
. B R . . . G G . B G R R . . 
. B G . . . R R . . . G . . R 
B G G R . . R G . . . B . . G 
G . R R . . G . . . . G . . G 
B B . R . . R . . B . R . G G 
. B . . . . . . . B . . G B B 

test2: 2/10
Votre sortie:
 .  .  .  .  .  .  .  .  .  . 
 .  .  .  .  R  .  .  .  .  . 
 .  .  .  .  .  R  .  R  .  . 
 .  .  .  R  B  .  .  .  .  R 
 .  R  R  R  R  .  .  .  B  R 
 R  .  .  .  B  .  .  .  .  R 
 R  .  .  .  B  .  .  .  .  . 
 R  R  .  B  .  .  .  .  .  R 
 .  .  R  R  B  .  R  .  R  R 
 .  .  .  R  R  R  .  .  .  . 

La réponse:
. . . . . . . . . . 
. . . . . . R . . . 
. . . . . . . R . . 
. . R R R . B R R . 
. . R . . . . . . . 
. . . R . . . . . . 
. . . R . . . . . . 
. . . R . B . . . . 
. . . R R R . . . . 
. . . . . . . . . . 

test3: 0/10
Votre sortie:
 .  .  .  .  . 
 .  B  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 

La réponse:
. . . . . 
. . . . . 
. . . . . 
. . . . . 
. . . . . 

test4: 10/10
Votre sortie:

test5: 6/10
Votre sortie:
 .  .  .  R  .  .  .  .  .  .  .  R  .  .  .  B  B  R  B  . 
 .  .  B  B  B  .  B  R  .  .  B  .  B  B  R  .  R  B  .  R 
 G  .  .  B  B  B  B  B  B  B  R  B  .  B  R  .  .  .  B  R 
 B  B  B  B  B  B  .  R  .  B  .  B  B  B  B  .  .  .  B  R 
 R  .  B  B  R  B  .  B  B  .  B  R  .  B  .  R  .  .  B  R 
 .  B  B  .  B  B  B  .  .  .  .  B  .  B  B  R  B  R  B  B 
 .  .  B  B  .  .  B  .  .  .  .  B  B  B  B  B  .  .  B  . 
 R  B  .  B  .  B  R  .  .  B  B  B  B  B  R  B  B  B  B  B 
 .  R  B  B  .  B  B  R  B  B  .  B  B  B  R  .  R  .  B  . 
 R  R  .  .  .  R  B  R  B  B  R  B  B  B  .  .  .  B  B  . 
 B  B  R  R  B  R  .  B  B  .  B  B  B  B  .  .  .  B  B  B 
 .  .  R  B  R  B  .  R  B  B  B  .  .  R  B  B  .  .  .  R 
 B  B  B  .  B  .  B  B  B  B  B  B  R  .  B  B  .  .  .  B 
 B  .  B  B  B  B  B  B  R  R  B  R  B  B  B  .  B  B  B  B 
 .  B  .  .  B  .  B  .  .  B  B  .  R  B  .  .  .  B  .  R 
 R  .  .  .  .  B  .  .  B  B  B  B  .  .  B  B  B  B  B  . 
 B  B  .  .  .  .  B  B  B  .  B  R  .  R  R  .  B  .  .  B 
 B  .  .  B  B  .  B  .  B  B  R  .  .  .  B  B  .  B  B  . 
 B  B  .  B  .  B  B  B  B  B  B  R  R  .  .  B  B  B  B  R 
 R  B  .  B  B  B  B  B  B  R  .  .  B  B  R  .  .  .  B  .

La réponse:
. . R R R . . . . . . . R R R B B . B . 
. . B B B . B . B B B . B B . . . B . R 
G . . B B B B B B B . B . B . B . B B . 
B B B B B B . . . B . B B B B R . R B . 
R . B B . B . B B R B . . B . . B . B . 
. B B . B B B B . . B B . B B . B . B B 
R . B B . . B R . . . B B B B B . . B . 
. B . B . B . . B B B B B B . B B B B B 
. . B B . B B . B B . B B B . . . . B B 
. . . . . . B . B B . B B B B . R B B B 
B B . . B . . B B . B B B B . . R B B B 
B . . B . B . . B B B . . . B B R . . R 
B B B . B . B B B B B B . . B B B R . B 
B . B B B B B B . . B . B B B B B B B B 
R B R B B . B . . B B . . B . . . B . R 
R B . . . B B . B B B B . . B B B B B R 
B B . . R B B B B . B . R R . . B . . B 
B . B B B . B . B B . . B B B B . B B B 
B B . B . B B B B B B . R . . B B B B R 
R B B B B B B B B . B B B B . R R B B R 

"""

