import game_board as gb
import user_input as ui
import copy

class Minimax:
    def __init__(self):
       pass

    def maximize(self, game_board = None, depth = 0):
        depth += 1

        if not game_board :
            game_board =  gb.GameBoard()
        if game_board.is_game_over():
            value = self.value(game_board)
            return value / depth, None
        if game_board.board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
            return 1000, 1
        
        best_value = -100000000
        for action in game_board.actions():
            new_game_board = game_board.make_copy()
            new_game_board.update_board(action)
            new_game_board.is_X_turn = not new_game_board.is_X_turn
            value = self.minimize(new_game_board, depth)[0]

            if value > best_value:
                best_value = value
                best_action = action
        return best_value, best_action

    def minimize(self, game_board = None, depth = 0):
        depth += 1
        if not game_board :
            game_board =  gb.GameBoard()

        if game_board.is_game_over():
            value = self.value(game_board)
            return value / depth, None
        
        best_value = 100000000
        for action in game_board.actions():
            new_game_board = game_board.make_copy()
            new_game_board.update_board(action)
            new_game_board.is_X_turn = not new_game_board.is_X_turn
            value = self.maximize(new_game_board, depth)[0]
           
            if value < best_value:
                best_value = value
                best_action = action
        return best_value, best_action

    def value(self, game_board):
        if self.X_wins(game_board):
            return 12
        elif self.O_wins(game_board):
            return -12
        elif self.is_tie(game_board):
            return 0

    def X_wins(self, game_board):
        return 'X' in (game_board.row_win(),
                       game_board.column_win(), 
                       game_board.diagonal_win())

    def O_wins(self, game_board):
        return 'O' in (game_board.row_win(), 
                       game_board.column_win(), 
                       game_board.diagonal_win())

    def is_tie(self, game_board):
        return game_board.is_tie()
      
