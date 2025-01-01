import unittest

import numpy as np

from Core.Domain.Vector2 import Vector2
from Core.Repository.PlayTable import PlayTable

class MyTestCase(unittest.TestCase):
    def test_init(self):
        print("Bad")
        self.Grid = PlayTable((2,2))
        for el in np.nditer(self.Grid.grid):
            self.assertTrue(el == 0)

        self.Grid.change_cell(Vector2(1,1), 2)
        self.assertEqual(self.Grid.grid[1,1], 2)
