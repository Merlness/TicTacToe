class Game_board:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
        self.is_X_turn = True

    def display(self):
        grid = "-------------\n"

        for row in self.board:
            for space in row:
                if isinstance(space, int):
                    grid += f"| {space} "
                else:
                    grid += self.place_XO(space)

            grid += "|\n" + "-------------\n"

        return grid

    def place_XO(self, space):
        if space == 'X':
            return "| \033[31mX\033[0m "
        if space == 'O':
            return "| \033[34mO\033[0m "
        
    def update_board(self, position):
        num = int(position)

        for row in self.board:
            if num  in row:
                row[row.index(num)] = self.change_XO()
        self.change_turn()

        return self.board

    def change_XO(self):
        if self.is_X_turn == True:
            return 'X'
        else:
            return 'O'
        
    def change_turn(self):
        self.is_X_turn = not self.is_X_turn



board =  Game_board()
print(board.display())
board.update_board(5)
board.update_board(6)
board.update_board(7)


print(board.display())

# def is_game_over(board):
#     if display_end_result(board) != False:
#         return True
#     return False

# def display_end_result(board):   
#     row_winner = row_win(board)
#     if row_winner:
#         return f"Congrats {row_win(board)} wins!"

#     column_winner = column_win(board)
#     if column_winner:
#         return f"Congrats {column_winner} wins!"

#     diagonal_winner = diagonal_win(board)
#     if diagonal_winner:
#         return f"Congrats {diagonal_winner} wins!"

#     if is_tie(board):
#         return 'Tie!'

#     return False

# def row_win(board):
#     for row in board:
#         letter = row[0]
#         game_over = all(element == letter for element in row)
        
#         if game_over:
#             return letter
#     return None

# def column_win(board):
#     for index in range(3):
#         letter = board[0][index]

#         if board[0][index] ==  board[1][index] ==  board[2][index]:
#             return letter
#     return None
    
# def diagonal_win(board):
#     letter = board[1][1]

#     if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
#         return letter
#     return None

# def is_tie(board):
#     if actions(board):
#         return False
#     return True

# def actions(board):
#     possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     actions = []

#     for row in board:
#         actions += [num for num in possibilities if num in row]
#     return actions
