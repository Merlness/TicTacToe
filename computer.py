# import user_input as ui
# import game_board as gb
# import console_user_interface as cgo
# import minimax as mm

import user_input as ui
import game_board as gb
import console_user_interface as cui
import helper as help
import minimax as mm

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game_board = gb.GameBoard(board)
interface_display = cui.ConsoleUserInterface()
number_of_moves = 0

# def play_computer(game_board, number_of_moves, X_turn):
#     while True:
#         print(gb.display_Game(game_board))

#         if X_turn:
#             ai_move = mm.minimax(game_board, number_of_moves, X_turn)[1] 
#             game_board = ui.update_board(ai_move, game_board, X_turn)
#         else:
#             game_board = ui.parse_input(game_board, X_turn)
       
#         if cgo.is_game_over(game_board):
#             congrats_message(game_board)
#             break
#         X_turn = not X_turn

def congrats_message(game_board):
    interface_display = cui.ConsoleUserInterface()
    display_board = interface_display.display(game_board)
    winning_message = help.Helper(game_board)
    return print(display_board + '\n' + winning_message.display_end_result())



while True:
        print(interface_display.display(game_board.board))

        if game_board.is_X_turn:
            # ai_move = mm.minimax(game_board, number_of_moves, X_turn)[1] 
            ai = mm.Minimax()
            ai_move = ai.maximize(number_of_moves)[1]

            game_board.board = ui.update_board(ai_move, game_board.board, game_board.is_X_turn)
        else:
            game_board.board = ui.parse_input( game_board.board, game_board.is_X_turn)
       
        if game_board.is_game_over():
            congrats_message(game_board.board)
            break
        
        game_board.is_X_turn = not game_board.is_X_turn


# def play_computer(game_board, number_of_moves, X_turn):
#     while True:
#         print(gb.display_Game(game_board))

#         if X_turn:
#             ai_move = mm.minimax(game_board, number_of_moves, X_turn)[1] 
#             game_board = ui.update_board(ai_move, game_board, X_turn)
#         else:
#             game_board = ui.parse_input(game_board, X_turn)
       
#         if cgo.is_game_over(game_board):
#             congrats_message(game_board)
#             break
#         X_turn = not X_turn

# def congrats_message(game_board):
#     display_board = gb.display_Game(game_board)
#     winning_message = cgo.display_end_result(game_board)
#     return print(display_board + '\n' + winning_message)
    
    