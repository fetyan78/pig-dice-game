import unittest
import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Sondos", False)
    
    def test_get_name(self):
            self.assertEqual(self.player.get_name(), "Sondos")
    
    def test_get_is_computer(self):
            self.assertFalse(self.player.get_is_computer())
    
    def test_set_name(self):
            self.player.set_name("Sara")
            self.assertEqual(self.player.get_name(), "Sara")
