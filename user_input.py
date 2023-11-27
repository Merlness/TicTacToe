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

