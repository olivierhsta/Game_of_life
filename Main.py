
from Rules import Rules
from Board import Board


rules = Rules()
dict_rules = Rules.read_rules(rules)
width_board, height_board = Rules.read_dimension(rules)
dict_position_cell = Rules.read_config(rules, dict_rules, width_board)

board = Board(dict_position_cell, width_board, height_board)

print(board)

