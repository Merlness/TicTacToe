import user_input as ui
import game_board as gb
import check_gameover as cgo
import minimax as mm

def play_computer(game_board, number_of_moves, X_turn):
    while True:
        print(gb.display_Game(game_board))

        if X_turn:
            ai_move = mm.minimax(game_board, number_of_moves, X_turn)[1] 
            game_board = ui.update_board(ai_move, game_board, X_turn)
        else:
            game_board = ui.parse_input(game_board, X_turn)
       
        if cgo.is_game_over(game_board):
            congrats_message(game_board)
            break
        X_turn = not X_turn

def congrats_message(game_board):
    display_board = gb.display_Game(game_board)
    winning_message = cgo.display_end_result(game_board)
    return print(display_board + '\n' + winning_message)
    