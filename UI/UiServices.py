from Core.Domain.Vector2 import Vector2
from .InputValidator import *
from .UiObject import UiObject


class Ui_Services():
    player = 1

    def __init__(self, UiObject: UiObject, core):
        self.UiObject = UiObject
        self.core = core

    def setupUi(self):
        size = self.UiObject.getBoardSize()
        try:
            size = validate_tuple([int, int], size)
            self.core.set_size(size)
        except ValidationError as V:
            print(V)
            self.setupUi()


    def __get_board(self):
        return self.core.get_board()

    def show_board(self):
        print(self.__get_board())

    def make_move(self):
        player = self.player
        try:
            location = validate_v2(int, self.UiObject.get_location())
            self.core.validate_move(player, location)
        except ValidationError as V:
            print(V)
            self.make_move()

    