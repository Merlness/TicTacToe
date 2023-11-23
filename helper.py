import game_board as gb

class Helper:
    def __init__(self, board):
        self.board = board

    def display_end_result(self):   
        game_board = gb.GameBoard(self.board)
        
        if game_board.find_winning_letter():
            return f"Congrats {game_board.find_winning_letter()} wins!"

        elif game_board.is_tie():
            return 'Tie!'

    
        
# place somehwere else
    # def parse_input(self, gboard):
    #     while True:
    #         position = self.get_position(gboard)
    #         update = gb.Game_board.update_board()
    #         board = update(position, gboard, self.is_X)
    #         if board:
    #             return board


#  def change_turn(self):
#         self.is_X_turn = not self.is_X_turn

