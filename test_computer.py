import unittest
import computer as sut
import io
from unittest.mock import patch


class MainTest(unittest.TestCase):
    pass
    # def verify_output(self,user_input,expected_output):
    #     with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         with patch('builtins.input', side_effect=user_input):
                # game_board_tie = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
                # sut.congrats_message(game_board_tie)

                # game_board_Xwin = [['X', 'O', 'X'], ['O', 5, 'X'], ['O', 8, 'X']]
                # sut.congrats_message(game_board_Xwin)

                # game_board_Owin = [['O', 'X', 'X'], ['O', 5, 6], ['O', 8, 9]]
                # sut.congrats_message(game_board_Owin)




    #         self.assertIn(expected_output, fake_stdout.getvalue())

    # def test_tie_gameboard(self):
    #     game_board = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
    #     expected_output = '-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m |\n-------------\n\nTie!\n'
    #     self.verify_output(game_board,expected_output)

    # def test_Xwin_gameboard(self):
    #     game_board = [['X', 'O', 'X'], ['O', 5, 'X'], ['O', 8, 'X']]
    #     expected_output = '-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[34mO\x1b[0m | 5 | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[34mO\x1b[0m | 8 | \x1b[31mX\x1b[0m |\n-------------\n\nCongrats X wins!\n'
    #     self.verify_output(game_board,expected_output)


    # def test_Owin_gameboard(self):
    #     game_board = [['O', 'X', 'X'], ['O', 5, 6], ['O', 8, 'X']]
    #     expected_output = '-------------\n| \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[34mO\x1b[0m | 5 | 6 |\n-------------\n| \x1b[34mO\x1b[0m | 8 | 9 |\n-------------\n\nCongrats O wins!\n'
    #     self.verify_output(game_board,expected_output)

if __name__ == '__main__':
    unittest.main()
    


