import copy

class GameBoard:
    def __init__(self, board = None, is_X_turn = True):
        self.is_X_turn = is_X_turn

        if board:
            #self.board = copy.deepcopy(board)
            self.board = board
        else:
            self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def update_board(self, position):
        num = int(position)

        for row in self.board:
            if num  in row:
                row[row.index(num)] = self.change_XO()
      
        return self.board

    def change_XO(self):
        if self.is_X_turn == True:
            return 'X'
        else:
            return 'O'

    def make_copy(self):
        return GameBoard(copy.deepcopy(self.board), self.is_X_turn)

    def row_win(self):
        for row in self.board:
            letter = row[0]
            game_over = all(element == letter for element in row)
            
            if game_over:
                return letter
        return None

    def column_win(self):
        board = self.board
        for index in range(3):
            letter = board[0][index]

            if board[0][index] ==  board[1][index] ==  board[2][index]:
                return letter
        return None

    def diagonal_win(self):
        board = self.board
        letter = board[1][1]

        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return letter
        return None

    def is_tie(self):
        return not self.actions()
        
    def actions(self):
        possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actions = []

        for row in self.board:
            actions += [num for num in possibilities if num in row]
        
        return actions
    
    def is_game_over(self):
        return (self.find_winning_letter() != False or self.is_tie())

    def find_winning_letter(self):   
        row_winner = self.row_win()
        if row_winner:
            return row_winner

        column_winner = self.column_win()
        if column_winner:
            return column_winner

        diagonal_winner = self.diagonal_win()
        if diagonal_winner:
            return diagonal_winner

        return False
