import game_board as gb



def parse_input(gbaord, isX):
    while True:
        position = get_position(gbaord)
        board = update_board(position, gbaord, isX)
        if board:
            return board


def update_board(position, board, isX):
    num = int(position)

    for row in board:
        if num  in row:
            row[row.index(num)] = change_XO(isX)
    # for row_index, row in enumerate(board):
    #     if num in row:
    #         col_index = row.index(num)
    #         board[row_index][col_index] = change_XO(isX)

    return board

def change_XO(isX):
    if isX == True:
        return 'X'
    else:
        return 'O'

def get_position(board):
    game_board = gb.GameBoard(board)    
    position = input("Enter your next move: ")
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    available_options = game_board.actions()

    if position in numbers and int(position) in available_options:
        return position

    return get_position(board)

# print(parse_input([[1, 2, 3], [4, 'X', 6], [7, 8, 9]], False))


# class Human:
#     def __init__(self):
#         pass
#         # self.is_x = is_x

#     def get_position(self, board):
#         position = input("Enter your next move: ")
#         numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#         available_options = gb.GameBoard.actions(board)
        
#         if position in numbers and int(position) in available_options:
#             return position
        
#         return self.get_position(board)
 
#     def parse_input(self, gboard):
#         #human_player = Human()
#         while True:
# #            position = human_player.get_position(gboard)
#             position = self.get_position(gboard)
#             #fix instance
#             update = gb.GameBoard.update_board(position)
#             # board = update(position, gboard, self.is_X)
#             board = update
#             if board:
#                 return board
            
# # human_instance = Human()
# #print(human_instance.parse_input([[1, 2, 3], [4, 'X', 6], [7, 8, 9]]))







# get a position from board based on token
#  - AI
#  - Human

# class AI:
#     def __init__(self, isX):
#         algo = minimax()

#     def get_position(board):
#         minimax.maximize(board)

# class Human:
#     def get_position(board):
#         pass

