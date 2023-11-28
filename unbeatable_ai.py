import computer as comp


class AI:
    def __init__(self):
        self.X_turn = True

    def get_user_turn(self):
        user = input("Would you like to go first, or second? Please Enter 1 or 2: ")

        while True:
            if user == '1':
                self.X_turn = False
                return self.X_turn
            elif user == '2':
                return self.X_turn
