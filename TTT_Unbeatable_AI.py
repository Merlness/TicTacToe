import computer as cf

game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
number_of_moves= 0
X_turn = True

def get_user_turn():
    User = input("Would you like to go first, or second? Please Enter 1 or 2: ")
    while True:
        if User == '1':
            return True
        elif User == '2':
           return False

if get_user_turn():
    X_turn = False


cf.play_computer(game_board, number_of_moves, X_turn)

