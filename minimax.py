import check_gameover as cg
import user_input as ui
import copy

def minimax(gamestate, depth ,isX):
    depth += 1

    if cg.is_game_over(gamestate):
        value = Value(gamestate)
        return value / depth, None

    if isX :
        best_value = -100000000
        for action in cg.actions(gamestate):
            new_gamestate = copy.deepcopy(gamestate)

            new_gamestate = ui.update_board(action, new_gamestate, isX)
            value = minimax(new_gamestate, depth, not isX)[0]
            if value > best_value:
                best_value = value
                best_action = action
        return best_value, best_action
    
    else:
        best_value = 100000000
        for action in cg.actions(gamestate):
            new_gamestate = copy.deepcopy(gamestate)
            new_gamestate = ui.update_board(action, new_gamestate, isX)
            value = minimax(new_gamestate, depth, not isX)[0]
            if value < best_value:
                best_value = value
                best_action = action
        return best_value, best_action


def Value(gamestate):
    X_won = False
    O_Won = False
    Tie = False

    if X_wins(gamestate):
        X_won = True
    elif O_wins(gamestate):
        O_Won = True
    elif is_Tie(gamestate):
        Tie = True

    if X_won:
        return 12
    if O_Won:
        return -12    
    if Tie:
        return 0

def X_wins(gamestate):
    if 'X' in (cg.row_win(gamestate), cg.column_win(gamestate), 
               cg.diagonal_win(gamestate)):
        return True
    return False

def O_wins(gamestate):
    if 'O' in (cg.row_win(gamestate), cg.column_win(gamestate), 
               cg.diagonal_win(gamestate)):
        return True
    return False

def is_Tie(gamestate):
    if cg.is_tie(gamestate):
        return True
    return False
