import numpy as np

from Core import *
from UI.TextUI import TextUI
from UI.UiServices import Ui_Services
from AI import ReversiAI
from Core.Domain.Vector2 import Vector2

core = Core()
ui_interface = TextUI()
ui = Ui_Services(ui_interface, core)
ui.setupUi()
AI = ReversiAI(2)

# The Game
while True:
    ui.show_board()
    p1_skip = False
    p2_skip = False
    if len(core.get_valid_moves(core.get_board(), 1)) != 0:
        try:
            ui.make_move()
        except MoveInvalidException as mi:
            print(mi)
            ui.make_move()
    else:
        p1_skip = True
        print("Player 1 can make no moves.\nSkipping Turn")

    ui.show_board()
    input("Show Ai Move ")
    if len(core.get_valid_moves(core.get_board(), 2)) != 0:
        board = core.get_board()
        move = AI.get_move(core, board)
        core.validate_move(AI.player_id, move)
    else:
        p2_skip = True
        print("Player 2 can make no moves.\nSkipping Turn")

    if p1_skip and p2_skip:
        # Game Over


