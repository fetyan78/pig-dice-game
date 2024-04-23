import unittest
import Scoreboard

class TestScoreboard(unittest.TestCase):
    
    def setUp(self): 
        self.players = ["Sara", "Sondos", "Ali"]
        self.scoreboard = Scoreboard(self.players)
