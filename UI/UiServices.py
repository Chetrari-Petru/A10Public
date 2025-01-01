from .InputValidator import *
from.UiObject import UiObject

class Ui_Services():
    def __init__(self, UiObject: UiObject, core):
        self.UiObject = UiObject
        self.core = core

    def setupUi(self):
        size = self.UiObject.getBoardSize()
        validate_tuple([int, int], size)

