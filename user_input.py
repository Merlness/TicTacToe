import game_board as gb
class UserInput:
    def __init__(self, board, isX):
        self.position = None
        self.board = board
        self.isX = isX
        
    def change_XO(self):
        if self.isX == True:
            return 'X'
        else:
            return 'O'

    def get_position(self):
        game_board = gb.GameBoard(self.board)
        position = input("Enter your next move: ")
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        available_options = game_board.actions()

        if position in numbers and int(position) in available_options:
            return position

        return self.get_position()
    def parse_input(self):
        while True:
            position = self.get_position()
            board = self.update_board(position)

            if board:
                return board

    def update_board(self, position):
        num = int(position)

        for row in self.board:
            if num in row:
                row[row.index(num)] = self.change_XO()

        return self.board

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

