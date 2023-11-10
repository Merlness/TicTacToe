import unittest
import game_board as sut

#python3 -m unittest 
class Test_Game_Board(unittest.TestCase):
    board = [[1, 2, 3], ['X', 'O', 6], [7, 8, 9]]

    def test_prints_numbers(self):
        numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
        view = any(item in numbers for item in sut.display_Game(self.board))       
        self.assertEqual(view, True)

    def test_empty_board(self):
        board = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
        view = sut.display_Game(board)
        top_border = "-------------\n"
        row_1 = "| 1 | 2 | 3 |\n" + "-------------\n"
        row_2 = "| 4 | 5 | 6 |\n" + "-------------\n"
        row_3 = "| 7 | 8 | 9 |\n"
        bottom_border = "-------------\n" 
        self.assertEqual(view, top_border + row_1 + row_2 + row_3 + bottom_border)

    def test_random_full_board(self):
        board = [ ['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
        view = sut.display_Game(board)
        top_border = "-------------\n"
        row_1 = "| \033[31mX\033[0m | \033[34mO\033[0m | \033[31mX\033[0m |\n" + "-------------\n"
        row_2 = "| \033[34mO\033[0m | \033[31mX\033[0m | \033[34mO\033[0m |\n" + "-------------\n"
        row_3 = "| \033[31mX\033[0m | \033[34mO\033[0m | \033[34mO\033[0m |\n"
        bottom_border = "-------------\n"
        self.assertEqual(view, top_border + row_1 + row_2 + row_3 + bottom_border)

 


# test display board (header to display tests)

# test an empty board
#test a board with X and O and make sure they are in correct spot when displayed

#printed_board = "--------"

if __name__ == '__main__':
    unittest.main()