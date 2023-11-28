import unbeatable_ai as ai
import computer as comp
import two_player as tp


class Main:

    def get_user_game(self):
        user = input("Would you like to play solo against the Unbeatable AI, or a two player game? \n"
                     "Please Enter 1 or 2: ")

        while True:
            if user == '1':
                return True
            elif user == '2':
                return False


if __name__ == "__main__":
    start_game = Main()
    AI_game = start_game.get_user_game()

    if AI_game:
        game = ai.AI()
        X_turn = game.get_user_turn()
        game_instance = comp.Computer(None, X_turn)
        game_instance.play_game()

    else:
        two_player_game = tp.TwoPlayer()
        two_player_game.play_game()
