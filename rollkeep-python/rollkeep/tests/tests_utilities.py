import unittest

from rollkeep.utilities import roll_dice

class TestUtilities(unittest.TestCase):
    
    def test_throw_invalid(self):
        with self.assertRaises(ValueError):
            roll_dice(0, 1)
        with self.assertRaises(ValueError):
            roll_dice(1, 0)
