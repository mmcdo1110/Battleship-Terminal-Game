import random

class Ship:
    def __init__(self, ship_name, num_spaces):
        self.name = ship_name
        self.spaces = num_spaces
        self.location_front = None
        self.location_back = None
        self.sunk = False

    def __repr__(self):
        return self.name
    
    def place_ship(self):
        coordinates = input("Please enter the starting coordinate of your ship: ")
        #Verifys that the coordinates were entered in the correct form.
        if len(coordinates) == 2:
            try:
                if 0 <= int(coordinates[1]) <= 9:
                    x = coordinates[1]
                    coordinates_ord = coordinates[0].upper()
                    if ord("A") <= ord(coordinates_ord) <= ord("J"):
                        y = coordinates[0]
                        self.location_front = coordinates
                        print(self.location_front)
                    else:
                        print("Must enter a letter A through J as the first coordinate character.")
            except ValueError:
                print("Must enter an integer as the second coordinate character.")
        else:
            print("Enter a coordinate that is two characters in length.")
            # self.place_ship()

#Define class objects for player 1's ships.
patrol1 = Ship("Patrol Boat", 2)
submarine1 = Ship("Submarine", 3)
destroyer1 = Ship("Destroyer", 3)
battleship1 = Ship("Battleship", 4)
carrier1 = Ship("Aircraft Carrier", 5)
player1_ships = [patrol1, submarine1, destroyer1, battleship1, carrier1]

#Define class objects for player 2's ships
patrol2 = Ship("Patrol Boat", 2)
submarine2 = Ship("Submarine", 3)
destroyer2 = Ship("Destroyer", 3)
battleship2 = Ship("Battleship", 4)
carrier2 = Ship("Aircraft Carrier", 5)
player2_ships = [patrol2, submarine2, destroyer2, battleship2, carrier2]


class Player:
    def __init__(self, name, ships):
        self.name = name.capitalize()
        self.available_ships = ships


#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name, player1_ships)
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name, player2_ships)


#Define a game of head or tails in order to determine who goes first.
def coin_flip():

    #The player to select heads or tails is also selected at random, adding another level of probability.
    players = [player1, player2]
    random_player = random.choice(players)

    #The selected player is asked to select head or tails from a terminal input.
    players_choice = input(random_player.name + " please select HEADS or TAILS: ")
    print(random_player.name + " you selected " + players_choice + ".")

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
print(coin_flip_winner.name + " goes first.\n")


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
print("\n" + coin_flip_winner.name + " time to place your ships.")
print("Available ships: " + str(coin_flip_winner.available_ships))
patrol1.place_ship()