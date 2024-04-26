import unittest
from unittest.mock import patch
from Terminal import Terminal

class TestTerminal(unittest.TestCase):
    def setUp(self):
        self.terminal = Terminal()

    def test_display_title(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_title()
            mock_print.assert_called_once()

    def test_display_intro_img(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_intro_img()
            mock_print.assert_called_once()

    def test_display_prompt(self):
        with patch('builtins.input', return_value='test_input'):
            result = self.terminal.display_prompt("Test prompt")
            self.assertEqual(result, 'test_input')

    def test_display_intro_menu(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_intro_menu()
            mock_print.assert_called_once()

    def test_display_computer_menu(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_computer_menu()
            mock_print.assert_called_once()

    def test_display_realtime_menu(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_realtime_menu()
            mock_print.assert_called_once()

    def test_display_rules(self):
        with patch('builtins.print') as mock_print:
            self.terminal.display_rules()
            mock_print.assert_called_once()

    def test_display_dice(self):
        with patch('builtins.print') as mock_print:
            faces_tuple = (1, 2)  # Exempel på tuple med tärningarnas värden
            self.terminal.display_dice(faces_tuple)
            self.assertEqual(mock_print.call_count, 2)  # Förväntar oss att print anropas två gånger

    def test_display_table(self):
        with patch('builtins.print') as mock_print:
            score_list = [["Player1", 10], ["Player2", 15]]  # Exempel på poänglista
            self.terminal.display_table(score_list)
            mock_print.assert_called_once()  # Förväntar oss att print anropas en gång

    def test_display_winner(self):
        with patch('builtins.print') as mock_print:
            player_name = "Player1"  # Exempel på vinnarnamn
            self.terminal.display_winner(player_name)
            mock_print.assert_called_once()  # Förväntar oss att print anropas en gång

    def test_display_clear(self):
        # Testmetoden för display_clear kan vara lite mer komplex att testa beroende på plattformen.
        # Vi kan dock testa att den anropar antingen 'clear' eller 'cls' beroende på plattformen.
        with patch('os.system') as mock_system:
            self.terminal.display_clear()
            platform = 'Windows'  # Exempel på plattformen
            if platform == 'Windows':
                mock_system.assert_called_once_with('cls')
            else:
                mock_system.assert_called_once_with('clear')

if __name__ == '__main__':
    unittest.main()
