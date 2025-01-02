from UI.UiObject import  UiObject
from Core.Domain.Vector2 import Vector2


class TextUI(UiObject):
    def getBoardSize(self):
        size = input("please _type the height of the board: ")
        size = (size, input("please _type the width of the board: "))
        return size

    def get_location(self):
       return Vector2(input("Please enter the x coordinate "), input("Please enter the y coordinate "))
