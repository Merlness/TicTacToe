
def parse_input(numbers, isX):
    while True:
        position = input("Enter your next move: ")
        num = update_board(position, numbers, isX)
        if num:
            return num


def update_board(position, numbers, isX):
    num = int(position)

    for row in numbers:
        if num  in row:
            row[row.index(num)] = change_XO(isX)
            isX = not isX
            return numbers


def change_XO(isX):
    if isX == True:
        return 'X'
    else:
        return 'O'