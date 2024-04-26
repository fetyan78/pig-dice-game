import unittest
from unittest.mock import Mock,patch
from io import StringIO
import Histogram

class TestHistogram(unittest.TestCase):
    def test_print_histogram(self):
        hist = Histogram()
        player1 = Mock()
        player1.get_name.return_value="Player1"
        player1.get_scoreList.return_value=[2,4,3]
        
        player2=Mock()
        player2.get_name.return_value = "Player2"
        player2.get_scoreList.return_value= [1, 6, 2]
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hist.print_histogram(player1, player2)
            expected_output = "\nPlayer1 got the following score within the game :\n" \
                              " *  * \n" \
                              " *  *  *  * \n" \
                              " *  *  * \n" \
                              "\nPlayer2 gReceived the following scores during the game :\n" \
                              " * \n" \
                              " *  *  *  *  *  * \n" \
                              " *  * \n" \
                              "\nNote that if there are 1 or 6 asterisks in a single row,means to start score from zero.\n"
            self.assertEqual(fake_out.getvalue(),expected_output)

if __name__ == '__main__':
    unittest.main()
