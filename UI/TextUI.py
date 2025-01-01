import UiObject


class TextUI(UiObject.UiObject):
    def getBoardSize(self):
        size = input("please type the height of the board: ")
        size = (size, input("please type the width of the board: "))
        return size
