import unittest
import user_input as sut
import game_board as gb

class Test_user_input(unittest.TestCase):
    def test_user_input(self):
        after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        board = gb.GameBoard()
        checkinput = board.update_board(5)
        self.assertEqual(checkinput, after_numbers)

    # def test_change_XO(self):
    #     after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 'O']]
    #     board = gb.GameBoard()
    #     board.update_board(5)
    #     gb.GameBoard().is_X_turn = False
    #     print(gb.GameBoard().is_X_turn)
    #     changed_board = board.update_board(9)
    #     self.assertEqual(changed_board, after_numbers)

    # def test_get_position(self):
    #     # board = gb.GameBoard()
    #     board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    #     user_input = sut.parse_input(board)
    #     # test = sut.Human.get_position(board)
    #     self.assertEqual('9', user_input)


if __name__ == '__main__':
    unittest.main()
