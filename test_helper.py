import unittest
import game_board as sut
import helper as help

#python3 -m unittest 

class TestHelper(unittest.TestCase):
    
    def test_display_X_winner(self):
        
        board = [['X', 'X', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        helper = help.Helper(board)
        check_game = helper.display_end_result()
        self.assertEqual(check_game, "Congrats X wins!")

    def test_display_O_winner(self):
        board = [[1, 2, 'O'],
                 [4, 'O', 6], 
                 ['O', 'X', 'X']]
        helper = help.Helper(board)
        check_game = helper.display_end_result()
        self.assertEqual(check_game, "Congrats O wins!")

    def test_display_tie(self):
        board = [['X', 'O', 'X'], 
                 ['O', 'X', 'X'], 
                 ['O', 'X', 'O']]
        helper = help.Helper(board)
        check_game = helper.display_end_result()
        self.assertEqual(check_game, "Tie!")
    
    



if __name__ == '__main__':
    unittest.main()
