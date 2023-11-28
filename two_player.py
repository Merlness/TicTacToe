import user_input as ui
import game_board as gb
import console_user_interface as cui
import helper


class TwoPlayer:
    def __init__(self):
        self.game_board = gb.GameBoard()
        self.interface_display = cui.ConsoleUserInterface()

    def play_game(self):
        while True:
            print(self.interface_display.display(self.game_board.board))
            user_input = ui.UserInput(self.game_board.board, self.game_board.is_x_turn)
            self.game_board.board = user_input.parse_input()

            if self.game_board.is_game_over():
                print(self.interface_display.display(self.game_board.board))
                end_board = helper.Helper(self.game_board.board)
                print(end_board.display_end_result())
                break

            self.game_board.is_x_turn = not self.game_board.is_x_turn
