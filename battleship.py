class Player:
    def __init__(self, name):
        self.name = name

#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name)
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name)

def print_blank_grid():
    for r in range(10):
        row = ""
        for c in range(10):
            row += "-"
        print(row)

print_blank_grid()