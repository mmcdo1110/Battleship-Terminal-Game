import random

class Player:
    def __init__(self, name):
        self.name = name

#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name)
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name)

#Define a game of head or tails in order to determine who goes first.
def heads_or_tails():

    #The player to select heads or tails is also selected at random, adding another level of probability.
    players = [player1_name, player2_name]
    random_player = random.choice(players)

    #The selected player is asked to select head or tails from a terminal input.
    players_choice = input(random_player + " please select HEADS or TAILS: ")
    print(random_player + " you selected " + players_choice + ".")

    #Randomly select heads or tails.
    heads_tails = ["HEADS", "TAILS"]
    result = random.choice(heads_tails)

    #Print the winning result.
    if result == players_choice.upper():
        print("The winner is " + result)
        winner = random_player
    else:
        print("The winner is " + result)
        players.remove(random_player)
        winner = players[0]

    print("The winner is " + winner + "!")

print("\nTime to determine who goes first.")
heads_or_tails()

def print_blank_grid():
    for r in range(10):
        row = ""
        for c in range(10):
            row += "-"
        print(row)

print_blank_grid()