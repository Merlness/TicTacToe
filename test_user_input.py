import unittest
import user_input as sut




class Test_user_input(unittest.TestCase):
    def test_user_input(self):
        before_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        checkinput = sut.update_board(5, before_numbers, True)
        self.assertEqual(checkinput, after_numbers)

    def test_change_XO(self):
        before_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        after_numbers = [[1, 2, 3], [4, 'X', 6], [7, 8, 'O']]
        changed_board = sut.update_board(9, before_numbers, False)
        self.assertEqual(changed_board, after_numbers)



if __name__ == '__main__':
    unittest.main()