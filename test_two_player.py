import io
import unittest
from unittest.mock import patch
import TTT_two_player as sut

class MainTest(unittest.TestCase):
    pass
    # def verify_output(self,user_input,expected_output):
    #     with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         with patch('builtins.input', side_effect=user_input):
    #             easy = [['X', 'O', 3], 
    #                     [4, 'X', 6], 
    #                     [7, 8, 9]]
                
    #             sut.play_two_people(easy, False)
                
                # difficult = [['X', 'O', 'X'], 
                #    [4, 5, 6], 
                #    [7, 8, 9]]
                
                # sut.play_two_people(difficult, False)
                

    #         self.assertIn(expected_output, fake_stdout.getvalue())

    # def test_two_player_easy(self):
    #     user_input = ['3', '9']
    #     expected_output = '-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | 3 |\n-------------\n| 4 | \x1b[31mX\x1b[0m | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[34mO\x1b[0m |\n-------------\n| 4 | \x1b[31mX\x1b[0m | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[34mO\x1b[0m |\n-------------\n| 4 | \x1b[31mX\x1b[0m | 6 |\n-------------\n| 7 | 8 | \x1b[31mX\x1b[0m |\n-------------\n\nCongrats X wins!\n'
    #     self.verify_output(user_input,expected_output)

    # def test_two_player_difficult(self):
    #     user_input = ['5', '4', '6', '7']
    #     expected_output = '-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| 4 | \x1b[34mO\x1b[0m | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | 6 |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[34mO\x1b[0m |\n-------------\n| 7 | 8 | 9 |\n-------------\n\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[31mX\x1b[0m |\n-------------\n| \x1b[31mX\x1b[0m | \x1b[34mO\x1b[0m | \x1b[34mO\x1b[0m |\n-------------\n| \x1b[31mX\x1b[0m | 8 | 9 |\n-------------\n\nCongrats X wins!\n'
    #     self.verify_output(user_input,expected_output)


if __name__ == '__main__':
    unittest.main()
    