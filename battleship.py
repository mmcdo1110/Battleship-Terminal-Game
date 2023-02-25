class Player:
    def __init__(self, name):
        self.name = name

player1 = input("Please enter the name of Player 1")

def print_blank_grid():
    for r in range(10):
        row = ""
        for c in range(10):
            row += "-"
        print(row)

print_blank_grid()