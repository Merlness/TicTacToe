import unittest
import check_gameover as sut

class Test_user_input(unittest.TestCase):
    #pass
    def test_first_rowX(self):
        first_row_X = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        check_game = sut.row_win(first_row_X)
        self.assertEqual(check_game, 'X')

    def test_seconod_rowX(self):
        second_row_X = [ [1, 2, 3],['X', 'X', 'X'], [7, 8, 9]]
        check_game = sut.row_win(second_row_X)
        self.assertEqual(check_game, "X")

    def test_third_rowO(self):
        third_row_O = [ [1, 2, 3],[4, 5, 6], ['O', 'O', 'O']]
        check_game = sut.row_win(third_row_O)
        self.assertEqual(check_game, "O")
    
    def test_first_columnO(self):
        first_column_O = [['O', 'X', 'X'], ['O', 5, 6], ['O', 8, 9]]
        check_game = sut.column_win(first_column_O)
        self.assertEqual(check_game, "O")

    def test_last_columnX(self):
        last_column_X = [['X', 'O', 'X'], ['O', 5, 'X'], ['O', 8, 'X']]
        check_game = sut.column_win(last_column_X)
        self.assertEqual(check_game, "X")

    def test_forward_diag_X(self):
        forward_diag_X = [['X', 'O', 'X'], 
                          ['O', 'X', 6], 
                          ['O', 8, 'X']]
        check_game = sut.diagonal_win(forward_diag_X)
        self.assertEqual(check_game, "X")

    def test_back_diag_O(self):
        back_diag_O = [ [1, 2, 'O'],
                       [4, 'O', 6], 
                       ['O', 'X', 'X']]
        check_game = sut.check_if_game_over(back_diag_O)
        self.assertEqual(check_game, "Congrats O wins!")

    def test_tie(self):
        Tie = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']]
        check_game = sut.is_tie(Tie)
        self.assertEqual(check_game, True)

    def test_not_a_tie(self):
        not_tie = [['X', 'O', 'X'], 
                   [4, 5, 6], 
                   [7, 8, 9]]
        check_game = sut.is_tie(not_tie)
        self.assertEqual(check_game, False)
  
    def test_edgecase_diag_X(self):
        edge_case = [['X', 2, 3], [4, 'X', 'O'], [7, 8, 9]]
        check_game = sut.diagonal_win(edge_case)
        self.assertEqual(check_game, None)
    

if __name__ == '__main__':
    unittest.main()

