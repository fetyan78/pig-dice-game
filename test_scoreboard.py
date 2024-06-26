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
    
    def test_update_score(self):
        self.scoreboard.update_score("Sara", 10)
        self.assertEqual(self.scoreboard.get_player("Sara")[1], 10)
        
        self.scoreboard.update_score("Sondos", 20)
        self.assertEqual(self.scoreboard.get_player("Sondos")[1], 20)

    def test_update_name(self):
        self.scoreboard.update_name("Sara", "Sarah")
        self.assertEqual(self.scoreboard.get_player("Sarah")[0], "Sarah")

    def test_reset_score(self):
        self.scoreboard.update_score("Sara", 10)
        self.scoreboard.resert_score("Sara")
        self.assertEqual(self.scoreboard.get_player("Sara")[1], 0)
    
    def test_get_winner(self):
        self.scoreboard.update_score("Sara", 100)
        self.assertEqual(self.scoreboard.get_winner(), "Sara")
    
    def test_get_player(self):
        player = self.scoreboard.get_player("Sara")
        self.assertEqual(player, ["Sara", 0])
    
    def test_get_scores(self):
        scores = self.scoreboard.get_scores()
        self.assertEqual(scores, [["Sara", 0], ["Sondos", 0], ["Ali", 0]])


if __name__ == '__main__':
    unittest.main()

    