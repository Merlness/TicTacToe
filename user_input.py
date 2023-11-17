import check_gameover as cg

def parse_input(gbaord, isX):
    while True:
        position = get_position(gbaord)
        board = update_board(position, gbaord, isX)
        if board:
            return board

    
def get_position(board):
    position = input("Enter your next move: ")
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    available_options = cg.actions(board)
    
    if position in numbers and int(position) in available_options:
        return position
    
    return get_position(board)


