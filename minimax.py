import game_board as gb
import user_input as ui
import copy

class Minimax:
    def __init__(self):
       pass

    def maximize(self, game_board = gb.GameBoard(), depth = 0):
        depth += 1

        if game_board.is_game_over():
            value = self.Value(game_board)
            return value / depth, None
        
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

    def minimize(self, game_board = gb.GameBoard(), depth = 0):
        depth += 1
        if game_board.is_game_over():
            value = self.Value(game_board)
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

    def Value(self, game_board):
        if self.X_wins(game_board):
            return 12
        elif self.O_wins(game_board):
            return -12
        elif self.is_Tie(game_board):
            return 0

    def X_wins(self, game_board):
        return 'X' in (game_board.row_win(),
                       game_board.column_win(), 
                       game_board.diagonal_win())

    def O_wins(self, game_board):
        return 'O' in (game_board.row_win(), 
                       game_board.column_win(), 
                       game_board.diagonal_win())

    def is_Tie(self, game_board):
        return game_board.is_tie()
      





# def minimax(board, depth ,isX):
#     depth += 1

#     if gb.GameBoard.is_game_over(board):
#         value = Value(board)
#         return value / depth, None

#     if isX :
#         best_value = -100000000
#         for action in gb.GameBoard.actions(board):
#             new_board = copy.deepcopy(board)

#             new_board = ui.update_board(action, new_board, isX)
#             value = minimax(new_board, depth, not isX)[0]
#             if value > best_value:
#                 best_value = value
#                 best_action = action
#         return best_value, best_action
    
#     else:
#         best_value = 100000000
#         for action in gb.GameBoard.actions(board):
#             new_board = copy.deepcopy(board)
#             new_board = ui.update_board(action, new_board, isX)
#             value = minimax(new_board, depth, not isX)[0]
#             if value < best_value:
#                 best_value = value
#                 best_action = action
#         return best_value, best_action


# def Value(board):
#     X_won = False
#     O_Won = False
#     Tie = False

#     if X_wins(board):
#         X_won = True
#     elif O_wins(board):
#         O_Won = True
#     elif is_Tie(board):
#         Tie = True

#     if X_won:
#         return 12
#     if O_Won:
#         return -12    
#     if Tie:
#         return 0

# def X_wins(board):
#     if 'X' in (gb.GameBoard.row_win(board), gb.GameBoard.column_win(board), 
#                gb.GameBoard.diagonal_win(board)):
#         return True
#     return False

# def O_wins(board):
#     if 'O' in (gb.GameBoard.row_win(board), gb.GameBoard.column_win(board), 
#                gb.GameBoard.diagonal_win(board)):
#         return True
#     return False

# def is_Tie(board):
#     if gb.GameBoard.is_tie(board):
#         return True
#     return False
