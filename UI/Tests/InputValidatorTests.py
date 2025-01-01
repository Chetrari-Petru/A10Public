import unittest
from UI.InputValidator import *

class ValidationTestCase(unittest.TestCase):
    def test_raises(self):
        print("Ad")
        self.assertRaises(SizeMismatchError, validate_tuple, [int, int], (1,))
        self.assertRaises(ValidationError, validate_tuple, [int, int], (1, 1.0))


if __name__ == '__main__':
    unittest.main()
