import math
import sys

from Blue import Blue
from Board import Board
from Green import Green
from Red import Red
from Rules import Rules

wait = False
bool_color = False
rep = 10

try:
    arg = sys.argv[1]
    try:
        rep = int(arg)
    except ValueError:
        rep = math.inf
        if arg == "animation":
            wait = True
        elif arg == "couleur":
            wait = False
            rep = 10
            bool_color = True
except IndexError:
    print("Aucun arguments entrees, 10 repetitions par defaut")

if bool_color:
    Red.show_color(Red)
    Blue.show_color(Blue)
    Green.show_color(Green)

rules = Rules()
dict_rules = Rules.read_rules(rules)

Red.BIRTH = dict_rules.get('R')[0]
Red.SURVIE = dict_rules.get('R')[1]
Red.DEATH = dict_rules.get('R')[-1]

Green.BIRTH = dict_rules.get('G')[0]
Green.SURVIE = dict_rules.get('G')[1]
Green.DEATH = dict_rules.get('G')[-1]

Blue.BIRTH = dict_rules.get('B')[0]
Blue.SURVIE = dict_rules.get('B')[1]
Blue.DEATH = dict_rules.get('B')[-1]

width_board, height_board = Rules.read_dimension(rules)
dict_position_cell = Rules.read_config(rules, dict_rules, width_board)

board = Board(dict_position_cell, width_board, height_board)
board.find_neigh()

i = 0
while i < rep:
    print(board)
    board.find_neigh()
    board.turn()
    i += 1
    if wait:
        input()
