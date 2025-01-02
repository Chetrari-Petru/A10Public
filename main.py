from Core import *
from UI.TextUI import TextUI
from UI.UiServices import Ui_Services

core = Core()
ui_interface = TextUI()
ui = Ui_Services(ui_interface, core)
ui.setupUi()


# The Game
while True:
    ui.show_board()
    try:
        ui.make_move()
        ui.player = (ui.player%2)+1
    except MoveInvalidException as mi:
        print(mi)
