import unittest
import game_board as sut

#python3 -m unittest 
class Test_Game_Board(unittest.TestCase):
    board = [[1, 2, 3], ['X', 'O', 6], [7, 8, 9]]

    def test_prints_numbers(self):
        numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
        gameboard = sut.Game_board()
        view = any(item in numbers for item in gameboard.display())  
        self.assertEqual(view, True)

    def test_empty_board(self):
        board = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        gameboard = sut.Game_board()
        view = gameboard.display()
        top_border = "-------------\n"
        row_1 = "| 1 | 2 | 3 |\n" + "-------------\n"
        row_2 = "| 4 | 5 | 6 |\n" + "-------------\n"
        row_3 = "| 7 | 8 | 9 |\n"
        bottom_border = "-------------\n" 
        self.assertEqual(view, top_border + row_1 + row_2 + row_3 + bottom_border)

    def test_random_full_board(self):
        gameboard = sut.Game_board()
        gameboard.board = [ ['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
        view = gameboard.display()
        top_border = "-------------\n"
        row_1 = "| \033[31mX\033[0m | \033[34mO\033[0m | \033[31mX\033[0m |\n" + "-------------\n"
        row_2 = "| \033[34mO\033[0m | \033[31mX\033[0m | \033[34mO\033[0m |\n" + "-------------\n"
        row_3 = "| \033[31mX\033[0m | \033[34mO\033[0m | \033[34mO\033[0m |\n"
        bottom_border = "-------------\n"
        self.assertEqual(view, top_border + row_1 + row_2 + row_3 + bottom_border)

class Test_board_endgame(unittest.TestCase):
    def test_first_rowX(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        check_game = gameboard.row_win()
        self.assertEqual(check_game, 'X')

    def test_second_rowX(self):
        gameboard = sut.Game_board()
        gameboard.board = [ [1, 2, 3],['X', 'X', 'X'], [7, 8, 9]]
        check_game = gameboard.row_win()
        self.assertEqual(check_game, "X")

    def test_third_rowO(self):
        gameboard = sut.Game_board()
        gameboard.board = [ [1, 2, 3],[4, 5, 6], ['O', 'O', 'O']]
        check_game = gameboard.row_win()
        self.assertEqual(check_game, "O")
    
    def test_first_columnO(self):
        gameboard = sut.Game_board()
        gameboard.board = [['O', 'X', 'X'], ['O', 5, 6], ['O', 8, 9]]
        check_game = gameboard.column_win()
        self.assertEqual(check_game, "O")

    def test_last_columnX(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], ['O', 5, 'X'], ['O', 8, 'X']]
        check_game = gameboard.column_win()
        self.assertEqual(check_game, "X")

    def test_forward_diag_X(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], 
                          ['O', 'X', 6], 
                          ['O', 8, 'X']]
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, "X")

    def test_back_diag_O(self):
        gameboard = sut.Game_board()
        gameboard.board = [ [1, 2, 'O'],
                       [4, 'O', 6], 
                       ['O', 'X', 'X']]
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, "O")

    def test_tie(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
        check_game = gameboard.is_tie()
        self.assertEqual(check_game, True)

    def test_not_a_tie(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], 
                   [4, 5, 6], 
                   [7, 8, 9]]
        check_game = gameboard.is_tie()
        self.assertEqual(check_game, False)
  
    def test_edgecase_diag_X(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 2, 3], [4, 'X', 'O'], [7, 8, 9]]
        check_game = gameboard.diagonal_win()
        self.assertEqual(check_game, None)

    def test_is_game_over(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, True)
    
    def test_is_game_over_not_yet(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], [4, 5, 6], [7, 8, 9]]
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, False)
    
    def test_is_game_over_tie(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
        check_game = gameboard.is_game_over()
        self.assertEqual(check_game, True)

    def test_find_winning_letter_X_row(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'X')

    def test_find_winning_letter_O_row(self):
        gameboard = sut.Game_board()
        gameboard.board = [ [1, 2, 3],[4, 5, 6], ['O', 'O', 'O']]
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'O')
    
    def test_find_winning_letter_O_column(self):
        gameboard = sut.Game_board()
        gameboard.board = [['O', 'X', 'X'], ['O', 5, 6], ['O', 8, 9]]
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'O')

    def test_find_winning_letter_X_diag(self):
        gameboard = sut.Game_board()
        gameboard.board = [['X', 'O', 'X'], 
                          ['O', 'X', 6], 
                          ['O', 8, 'X']]
        check_game = gameboard.find_winning_letter()
        self.assertEqual(check_game, 'X')



if __name__ == '__main__':
    unittest.main()
