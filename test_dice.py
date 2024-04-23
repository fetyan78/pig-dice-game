import unittest
import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        result = self.dice.roll()
        rolls = result['rolls']
        total = result['total']
        self.assertIsInstance(rolls, tuple)
        self.assertEqual(len(rolls), 2)
        self.assertTrue(1 <= rolls[0] <= 6)
        self.assertTrue(1 <= rolls[1] <= 6)
        self.assertTrue(2 <= total <= 12)           
    if __name__ == '__main__':
        unittest.main()