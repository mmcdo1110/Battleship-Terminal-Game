import random


class Player:
    def __init__(self, name):
        self.name = name.capitalize()


#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name)
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name)


#Define a game of head or tails in order to determine who goes first.
def coin_flip():

    #The player to select heads or tails is also selected at random, adding another level of probability.
    players = [player1.name, player2.name]
    random_player = random.choice(players)

    #The selected player is asked to select head or tails from a terminal input.
    players_choice = input(random_player + " please select HEADS or TAILS: ")
    print(random_player + " you selected " + players_choice + ".")

    #Randomly select heads or tails.
    heads_tails = ["HEADS", "TAILS"]
    result = random.choice(heads_tails)

    #Print the winning result.
    if result == players_choice.upper():
        print("The coin landed on " + result + "!")
        winner = random_player
    else:
        print("The coin landed on " + result + "!")
        players.remove(random_player)
        winner = players[0]
    return winner 


print("\nTime to determine who goes first.")
coin_flip_winner = coin_flip()
print(coin_flip_winner + " goes first.\n")


def print_blank_grid():
    first_row = "  "
    for i in range(1, 10):
        first_row += " {} ".format(i)
    first_row += " 0 "
    print(first_row)
    for r in range(10):
        letter = chr(ord("A") + r)
        row = letter + " "
        for c in range(10):
            row += " - "
        print(row)

print_blank_grid()
print("\n" + coin_flip_winner + " time to place your ships.")