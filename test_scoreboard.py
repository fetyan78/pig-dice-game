import unittest
import Scoreboard

class TestScoreboard(unittest.TestCase):
    
    def setUp(self): 
        self.players = ["Sara", "Sondos", "Ali"]
        self.scoreboard = Scoreboard(self.players)
    
    def test_initialization(self):
        self.assertEqual(self.scoreboard.maximum_score, 100)
        self.assertIsNone(self.scoreboard.wining_player)
        self.assertEqual(self.scoreboard.player_scores, [["Sara", 0], ["Sondos", 0], ["Ali", 0]])