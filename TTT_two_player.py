import user_input as ui
import console_user_interface as cui
import game_board as gb
import console_user_interface as cgo
import computer as c

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
is_X_turn = True

def play_two_people(game_board, X_turn):
    while True:
        print(cui.ConsoleUserInterface.display(game_board))
        user_input = ui.UserInput(game_board, X_turn)
        game_board = user_input. parse_input()

        if cgo.is_game_over(game_board):
            c.congrats_message(game_board)
            break
        X_turn = not X_turn


play_two_people(board, is_X_turn)