import user_input as ui
import game_board as gb
import console_user_interface as cui
import helper as help


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game_board = gb.GameBoard(board)
interface_display = cui.ConsoleUserInterface()

while True:
    print(interface_display.display(game_board.board))
    game_board = game_board.update_board(game_board)
    if game_board.is_game_over():
        print(interface_display.display(game_board.board))
        print(help.Helper.display_end_result())

        break
    X_turn = not X_turn

