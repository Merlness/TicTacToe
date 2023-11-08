import check_gameover as cg
import user_input as ui

#minmax maxs for X mins for O
def minimax(gamestate, isX):
    if cg.check_if_game_over(gamestate):
        return Value(gamestate, isX)
    
    if isX :
        value = -100000000
        for action in cg.actions(gamestate):
            value = max(value, minimax(result(gamestate, action, isX)))
        return value
    
    else:
        value = 100000000
        for action in cg.actions(gamestate):
            value = min(value, minimax(result(gamestate, action, isX)))
        return value


def Value(gamestate, isX):
    X_wins = False
    O_wins = False
    Tie = False

    if cg.check_if_game_over(gamestate) == "Congrats X wins!":
        X_wins = True
    elif cg.check_if_game_over(gamestate) == "Congrats O wins!":
        O_wins = True
    elif cg.check_if_game_over(gamestate) == 'Tie!':
        Tie = True

    if X_wins and isX:
            return 1
    if X_wins and not isX:
        return -1
    if O_wins and isX:
        return -1
    if O_wins and not isX:
        return 1
    if Tie:
        return 0

#similar to update board
def result(gamestate, action, isX):
    new_gamestate = gamestate.copy()
    num = int(action)

    for row in new_gamestate:
        if num  in row:
            row[row.index(num)] = ui.change_XO(isX)
            isX = not isX
            return new_gamestate, isX
