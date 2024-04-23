import unittest
import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Sondos", False)
    
    def test_get_name(self):
            self.assertEqual(self.player.get_name(), "Sondos")