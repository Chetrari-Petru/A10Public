import numpy as np
from Core.Domain.Vector2 import Vector2


class PlayTable:
    """
    A field of playable grid
    """
    def __init__(self, size):
        self.grid = np.zeros(size, dtype=np.int8)

    def change_cell(self, position: Vector2, value: int):
        """
        Changes the value of the specified cell
        :param position: Position of the cell
        :param value: The value to be written
        """
        self.grid[position.x, position.y] = value