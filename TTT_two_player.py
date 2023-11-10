import user_input as ui
import game_board as gb
import check_gameover as cgo
import computer as c

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
is_X_turn = True

def play_two_people(game_board, X_turn):
    while True:
        print(gb.display_Game(game_board))
        game_board = ui.parse_input(game_board, X_turn)
       
        if cgo.is_game_over(game_board):
            c.congrats_message(game_board)
            break
        X_turn = not X_turn


play_two_people(board, is_X_turn)