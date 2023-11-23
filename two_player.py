import user_input as ui
import game_board as gb
import console_user_interface as cui
import helper as help


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game_board = gb.GameBoard(board)
interface_display = cui.ConsoleUserInterface()

while True:
    print(interface_display.display(game_board.board))
    game_board.board = ui.parse_input( game_board.board, game_board.is_X_turn)

    if game_board.is_game_over():
        print(interface_display.display(game_board.board))
        end_board = help.Helper(board)
        print(end_board.display_end_result())

        break
    game_board.is_X_turn = not game_board.is_X_turn

# def play_two_people(game_board, X_turn):
#     while True:
#         print(gb.display_Game(game_board))
#         game_board = ui.parse_input(game_board, X_turn)

#         if cgo.is_game_over(game_board):
#             c.congrats_message(game_board)
#             break
#         X_turn = not X_turn