# import unittest
# import minimax as sut

# class Test_minimax(unittest.TestCase): 
#     def test_end_move(self):
#         board = [['X', 2, 3], 
#                 ['O', 'X', 6], 
#                 ['O', 8, 9]]
#         actual_value = sut.minimax(board, 0, True)[1]
#         self.assertEqual(actual_value, 9)

#     def test_block(self):
#         board = [[1, 2, 3], 
#                 ['O', 'X', 'X'], 
#                 ['O', 8, 9]]
#         actual_value = sut.minimax(board, 0, True)[1]
#         self.assertEqual(actual_value, 1)
        
#     def test_optimal_move(self):
#         board = [['X', 2, 3], 
#                 ['O', 5, 6], 
#                 [7, 8, 9]]
#         actual_value = sut.minimax(board, 0, True)[1]
#         possible_expected_values = [2, 3]
#         found_match = any(actual_value == expected for expected in possible_expected_values)
#         self.assertTrue(found_match)

#     def test_end_moves(self):
#         board = [['X', 'X', 'O'], 
#                 ['O', 'X', 6], 
#                 ['O', 8, 9]]
#         actual_value = sut.minimax(board, 0, True)[1]
#         possible_expected_values = [8, 9]
#         found_match = any(actual_value == expected for expected in possible_expected_values)
#         self.assertTrue(found_match)

        # def test_first_move(self):
        #     clean_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        #     actual_value = sut.minimax(clean_board, 0, True)[1]
        #     possible_expected_values = [1, 3, 7, 9]
        #     found_match = any(actual_value == expected for expected in possible_expected_values)
        #     self.assertTrue(found_match)

if __name__ == '__main__':
    unittest.main()

