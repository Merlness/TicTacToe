import game_board as gb
import console_user_interface as cui
import minimax as mm
import user_input as ui
import helper as help

class Computer:
    def __init__(self, board):
        self.game_board = gb.GameBoard(board)
        self.interface_display = cui.ConsoleUserInterface()
        self.number_of_moves = 0

    def play_game(self):
        while True:
            print(self.interface_display.display(self.game_board.board))

            if self.game_board.is_X_turn:
                ai = mm.Minimax()
                ai_move = ai.maximize(self.game_board, self.number_of_moves)[1]
                user_input = ui.UserInput(self.game_board.board, self.game_board.is_X_turn)
                self.game_board.board = user_input.update_board(ai_move)
            else:
                user_input = ui.UserInput(self.game_board.board, self.game_board.is_X_turn)
                self.game_board.board = user_input.parse_input()

            if self.game_board.is_game_over():
                winning_message = help.Helper(self.game_board.board)
                winning_message.congrats_message()
                break

            self.game_board.is_X_turn = not self.game_board.is_X_turn

if __name__ == "__main__":
    initial_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game_instance = Computer(initial_board)
    game_instance.play_game()

