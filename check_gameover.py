def check_if_game_over(board):   
    if row_win(board):
        return f"Congrats {row_win(board)} wins!"
           
    if column_win(board):
        return f"Congrats {column_win(board)} wins!"
    
    if diagonal_win(board):
        return f"Congrats {diagonal_win(board)} wins!"

    if is_tie(board): 
        return 'Tie!'

    return False

def row_win(board):
    for row in board:
        letter = row[0]
        game_over = all(element == letter for element in row)
        
        if game_over:
            return letter

def column_win(board):
    for index in range(3):
        letter = board[0][index]

        if board[0][index] ==  board[1][index] ==  board[2][index]:
            return letter

def diagonal_win(board):
    letter = board[1][1]
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return letter

def is_tie(board):
    if actions(board):
        return False
    return True

def actions(board):
    possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actions = []
    for row in board:
        actions += [num for num in possibilities if num in row]
    return actions