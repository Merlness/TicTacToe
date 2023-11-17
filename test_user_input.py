import unittest
import user_input as sut
import game_board as gb

class Test_user_input(unittest.TestCase):
    def test_user_input(self):
        after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        board = gb.Game_board()
        checkinput = board.update_board(5)
        self.assertEqual(checkinput, after_numbers)

    def test_change_XO(self):
        after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 'O']]
        board = gb.Game_board()
        board.update_board(5)
        changed_board = board.update_board(9)
        self.assertEqual(changed_board, after_numbers)

if __name__ == '__main__':
    unittest.main()
