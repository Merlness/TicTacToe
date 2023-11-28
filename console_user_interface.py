class ConsoleUserInterface:

    def display(self, board):
        grid = "-------------\n"

        for row in board:
            for space in row:
                if isinstance(space, int):
                    grid += f"| {space} "
                else:
                    grid += self.place_xo(space)

            grid += "|\n" + "-------------\n"

        return grid

    def place_xo(self, space):
        if space == 'X':
            return "| \033[31mX\033[0m "
        if space == 'O':
            return "| \033[34mO\033[0m "

