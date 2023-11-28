import game_board as gb
import console_user_interface as cui
import minimax as mm
import user_input as ui
import helper as helper


class Computer:
    def __init__(self, board = None, is_x_turn = True):
        self.is_x_turn = is_x_turn

        if board:
            self.board = board
        else:
            self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.game_board = gb.GameBoard(board, self.is_x_turn)
        self.interface_display = cui.ConsoleUserInterface()
        self.number_of_moves = 0

    def play_game(self):
        while True:
            print(self.interface_display.display(self.game_board.board))

            if self.game_board.is_x_turn:
                ai = mm.Minimax()
                ai_move = ai.maximize(self.game_board, self.number_of_moves)[1]
                user_input = ui.UserInput(self.game_board.board, self.game_board.is_x_turn)
                self.game_board.board = user_input.update_board(ai_move)
            else:
                user_input = ui.UserInput(self.game_board.board, self.game_board.is_x_turn)
                self.game_board.board = user_input.parse_input()

            if self.game_board.is_game_over():
                winning_message = helper.Helper(self.game_board.board)
                winning_message.congrats_message()
                break

            self.game_board.is_x_turn = not self.game_board.is_x_turn

#
# if __name__ == "__main__":
#     game_instance = Computer()
#     game_instance.play_game()

# main.py
# ui = ConsoleInterface()
# board = gb.GameBoard()
# player_1 = Human()
# if computer:
#     player_2 = Computer()
# else:
#     player_2 = Human()
#
# while not game.is_over():
#     game.play(ui, board, player_1, player_2)
#
# ui.display_winner(board)
