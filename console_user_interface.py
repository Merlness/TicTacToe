# rows = board.get_rows() => [[1, 2, 3], ['x', 'o', 6], ['x', 'o', 'x']]
# ui.present(rows) => print(xs and os to console)

#console ui  display and XO
class ConsoleUserInterface:

    def display(self, board):
        grid = "-------------\n"

        for row in board:
            for space in row:
                if isinstance(space, int):
                    grid += f"| {space} "
                else:
                    grid += self.place_XO(space)

            grid += "|\n" + "-------------\n"

        return grid

    def place_XO(self, space):
        if space == 'X':
            return "| \033[31mX\033[0m "
        if space == 'O':
            return "| \033[34mO\033[0m "

