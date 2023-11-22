import game_board as gb

class Helper:
    def __init__(self):
        pass
        # self.is_X_turn = is_X

    def display_end_result(self):   
        game_board = gb.GameBoard()
        
        if game_board.find_winning_letter():
            return f"Congrats {game_board.find_winning_letter()} wins!"

        # row_winner = row_win(board)
        # if row_winner:
        #     return f"Congrats {row_win(board)} wins!"

        # column_winner = column_win(board)
        # if column_winner:
        #     return f"Congrats {column_winner} wins!"

        # diagonal_winner = diagonal_win(board)
        # if diagonal_winner:
        #     return f"Congrats {diagonal_winner} wins!"

        elif gb.GameBoard.is_tie():
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

#place elsewhere

