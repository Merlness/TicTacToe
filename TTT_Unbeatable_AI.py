import computer as comp


class AI:
    def __init__(self):
        pass
        self.X_turn = True

    def get_user_turn(self):
        user = input("Would you like to go first, or second? Please Enter 1 or 2: ")

        while True:
            if user == '1':
                self.X_turn = False
                return self.X_turn
            elif user == '2':
                return self.X_turn


if __name__ == "__main__":
    start_game = AI()
    X_turn = start_game.get_user_turn()
    game_instance = comp.Computer(None, X_turn)
    game_instance.play_game()
