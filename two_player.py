import user_input as ui
import game_board as gb
import check_gameover as go

game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
X_turn = True

while True:
    print(gb.display_Game(game_board))
    game_board = ui.update_board(game_board, X_turn)
    if go.check_if_game_over(game_board):
        print(gb.display_Game(game_board))
        print(go.check_if_game_over(game_board))

        break
    X_turn = not X_turn
