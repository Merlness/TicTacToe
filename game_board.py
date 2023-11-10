def display_Game(gboard):
    grid = "-------------\n"

    for row in gboard:
        for space in row:
            if isinstance(space, int):
                grid += f"| {space} "
            else:
                grid += place_XO(space, grid)

        grid += "|\n" + "-------------\n"

    return grid

def place_XO(space, grid):
    if space == 'X':
        return "| \033[31mX\033[0m "
    if space == 'O':
        return "| \033[34mO\033[0m "

