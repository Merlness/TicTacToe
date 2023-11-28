import unittest
import game_board as sut
#python3 -m unittest


class TestBoardEndgame(unittest.TestCase):
    def test_first_rowX(self):
        board = [['X', 'X', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.row_win()
        self.assertEqual(check_game, 'X')

    def test_second_rowX(self):
        board = [[1, 2, 3],
                 ['X', 'X', 'X'], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.row_win()
        self.assertEqual(check_game, "X")

    def test_third_rowO(self):
        board = [[1, 2, 3],
                 [4, 5, 6], 
                 ['O', 'O', 'O']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.row_win()
        self.assertEqual(check_game, "O")
    
    def test_first_columnO(self):
        board = [['O', 'X', 'X'], 
                 ['O', 5, 6], 
                 ['O', 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.column_win()
        self.assertEqual(check_game, "O")

    def test_last_columnX(self):
        board = [['X', 'O', 'X'], 
                 ['O', 5, 'X'], 
                 ['O', 8, 'X']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.column_win()
        self.assertEqual(check_game, "X")

    def test_forward_diag_X(self):
        board = [['X', 'O', 'X'], 
                 ['O', 'X', 6], 
                 ['O', 8, 'X']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, "X")

    def test_back_diag_O(self):
        board = [[1, 2, 'O'],
                 [4, 'O', 6], 
                 ['O', 'X', 'X']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, "O")

    def test_tie(self):
        board = [['X', 'O', 'X'], 
                 ['O', 'X', 'X'], 
                 ['O', 'X', 'O']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.is_tie()
        self.assertEqual(check_game, True)

    def test_not_a_tie(self):
        board = [['X', 'O', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.is_tie()
        self.assertEqual(check_game, False)
  
    def test_edgecase_diag_X(self):
        board = [['X', 2, 3], 
                 [4, 'X', 'O'], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, None)

    def test_is_game_over(self):
        board = [['X', 'X', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, True)
    
    def test_is_game_over_not_yet(self):
        board = [['X', 'O', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, False)
    
    def test_is_game_over_tie(self):
        board = [['X', 'O', 'X'], 
                 ['O', 'X', 'X'], 
                 ['O', 'X', 'O']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, True)

    def test_find_winning_letter_X_row(self):
        board = [['X', 'X', 'X'], 
                 [4, 5, 6], 
                 [7, 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'X')

    def test_find_winning_letter_O_row(self):
        board = [ [1, 2, 3],
                  [4, 5, 6], 
                  ['O', 'O', 'O']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'O')
    
    def test_find_winning_letter_O_column(self):
        board = [['O', 'X', 'X'], 
                 ['O', 5, 6], 
                 ['O', 8, 9]]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'O')

    def test_find_winning_letter_X_diag(self):
        board = [['X', 'O', 'X'], 
                 ['O', 'X', 6], 
                 ['O', 8, 'X']]
        gameboard = sut.GameBoard(board)
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'X')
  

if __name__ == '__main__':
    unittest.main()
