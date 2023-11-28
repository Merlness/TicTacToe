import game_board as gb
import console_user_interface as cui


class Helper:
    def __init__(self, board):
        self.board = board
        self.game_board = gb.GameBoard(self.board)

    def display_end_result(self):   
        if self.print_winner():
            return self.print_winner()
        
        elif self.game_board.is_tie():
            return '\033[35mTie!\033[0m'

    def print_winner(self):
        letter = self.game_board.find_winning_letter()

        if letter == 'X':
            return f"\033[31mCongrats {letter} wins!\033[0m"
        elif letter == 'O':
            return f"\033[34mCongrats {letter} wins!\033[0m"

    def congrats_message(self):
        interface_display = cui.ConsoleUserInterface()
        display_board = interface_display.display(self.board)
        return print(display_board + '\n' + self.display_end_result())
