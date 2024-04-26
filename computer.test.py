import unittest
from unittest.mock import patch
from random import shuffle
import Computer

class TestComputer(unittest.TestCase):
    def setUp(self):
        self.comp = Computer(2)

    def test_init(self):
        self.assertEqual(self.comp.difficulty_level, 2)
        self.assertTrue(0 < self.comp.probability < 1)
        self.assertIsInstance(self.comp.biased_list, list)
        self.assertIsInstance(self.comp.decision_list, list)

    def test_get_difficulty_level(self):
        self.assertEqual(self.comp.get_difficulty_level(), 2)

    def test_set_difficulty(self):
        self.comp.set_difficulty(3)
        self.assertEqual(self.comp.difficulty, 3)

    def test_get_probability(self):
        self.assertTrue(0 < self.comp.get_probability() < 1)

    def test_generate_biased_list(self):
        biased_list = self.comp.generate_biased_list()
        self.assertIsInstance(biased_list, list)
        self.assertGreater(len(biased_list), 0)

    def test_get_biased_list(self):
        self.assertIsInstance(self.comp.get_biased_list(), list)

    def test_generate_decision_list(self):
        with patch('random.shuffle') as mock_shuffle:
            self.comp.generate_decision_list()
            self.assertTrue(mock_shuffle.called)

    def test_get_decision_list(self):
        self.assertIsInstance(self.comp.get_decision_list(), list)


if __name__ == '__main__':
    unittest.main()
