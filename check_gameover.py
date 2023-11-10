def is_game_over(board):
    if display_end_result(board) != False:
        return True
    return False

def display_end_result(board):   
    row_winner = row_win(board)
    if row_winner:
        return f"Congrats {row_win(board)} wins!"

    column_winner = column_win(board)
    if column_winner:
        return f"Congrats {column_winner} wins!"

    diagonal_winner = diagonal_win(board)
    if diagonal_winner:
        return f"Congrats {diagonal_winner} wins!"

    if is_tie(board):
        return 'Tie!'

    return False

def row_win(board):
    for row in board:
        letter = row[0]
        game_over = all(element == letter for element in row)
        
        if game_over:
            return letter
    return None

def column_win(board):
    for index in range(3):
        letter = board[0][index]

        if board[0][index] ==  board[1][index] ==  board[2][index]:
            return letter
    return None
    
def diagonal_win(board):
    letter = board[1][1]

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return letter
    return None

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
