import random


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


class Ship:
    def __init__(self, ship_name, ship_length):
        self.name = ship_name
        self.length = ship_length
        self.location_front = None
        self.location_back = None
        self.sunk = False

    def __repr__(self):
        return self.name

    def front_back_dist_check(self, ship_length, front_coord, back_coord):
        front_x = front_coord[0]
        front_y = int(front_coord[1])
        back_x = back_coord[0]
        back_y = int(back_coord[1])
        length = ship_length
        if (ord(front_x) + (length - 1)) == ord(back_x) or (ord(front_x) - (length -1)) == ord(back_x):
            pass
        elif ((front_y) + (length - 1)) == back_y or ((front_y) - (length - 1)) == back_y:
            pass
        else:
            print("The distance between entered coordinates is greater than ship's length. Please re-enter your coordinates.")

    
    def set_ship(self):
        front_coords = input("Please enter the starting coordinates of your ship: ")
        #Verifys that the coordinates were entered in the correct form.
        if len(front_coords) == 2:
            if ord("A") <= ord(front_coords[0].upper()) <= ord("J"):
                front_x = front_coords[0]
                self.location_front = front_coords 
                try:
                    if 0 <= int(front_coords[1]) <= 9:
                        front_y = int(front_coords[1])
                        back_coords = input("Please enter the ending coordinates of your ship: ")
                        if len(back_coords) == 2:
                            if ord("A") <= ord(back_coords[0].upper()) <= ord("J"):
                                back_x = back_coords[0]
                                self.location_back = back_coords
                                try:    
                                    if 0 <= int(back_coords[1]) <= 9:
                                        back_y = int(back_coords[1])
                                        if (ord(front_x) + (self.length - 1)) == ord(back_x) and (front_y == back_y) or (ord(front_x) - (self.length - 1)) == ord(back_x) and (front_y == back_y):
                                            pass
                                        elif (front_y + (self.length - 1)) == back_y and (front_x == back_x) or (front_y - (self.length - 1)) == back_y and (front_x == back_x):
                                            pass
                                        else:
                                            print("Out of range")
                                            self.set_ship()
                                        print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
                                except ValueError:
                                    print("**Must enter an integer as the second coordinate character.**\n")
                                    self.set_ship()
                            else:
                                print("**Must enter a letter A through J as the first coordinate character.**\n")
                                self.set_ship()
                        else:
                            print("**Enter a coordinate that is two characters in length.**\n")
                            self.set_ship()
                    else:
                        raise ValueError
                except ValueError:
                    print("**Must enter an integer as the second coordinate character.**\n")
                    self.set_ship()
            else:
                print("**Must enter a letter A through J as the first coordinate character.**\n")
                self.set_ship()
        else:
            print("**Enter a coordinate that is two characters in length.**\n")
            self.set_ship()
        
        

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
        self.placed_ships = None


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
    print(random_player.name + " you selected " + players_choice + ".\n")

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


print_blank_grid()
# print("\n" + coin_flip_winner.name + " time to place your ships.")
# print(coin_flip_winner.name + "'s available ships: " + str(coin_flip_winner.available_ships))
# patrol1.set_front()
# print(patrol1.location_front)
# patrol1.set_back()
patrol1.set_ship()
