import random

def new_grid_data():
    grid_data = []
    first_row = ["  "]
    for i in range(1, 10):
        first_row.append(" {} ".format(i))
    first_row.append(" {} ".format(0))
    grid_data.append(first_row)
    for r in range(10):
        new_row = []
        new_row.append(chr(ord("A") + r) + " ")
        for c in range(10):
            new_row.append(" - ")
        grid_data.append(new_row)
    return grid_data

def print_grid(grid_data):
    print("\n")
    for row in grid_data:
        print_row = ""
        for col in row:
            add_col = col
            print_row += add_col
        print(print_row)
    print("\n")

def add_ship_to_grid(ship, grid_data):
    front_x = (ord(ship.location_front[0]) - 64)  #B
    front_y = int(ship.location_front[1])         #6
    back_x = (ord(ship.location_back[0]) - 64)    #D
    back_y = int(ship.location_back[1])           #6

    grid_data[front_x][front_y] = "[ ]"
    grid_data[back_x][back_y] = "[ ]"
    
    dist_x = (back_x - front_x)
    dist_y = (back_y - front_y)

    if dist_x == 0:
        if dist_y > 0:
            for i in range(dist_y):
                grid_data[front_x][front_y + i] = "[ ]"
        elif dist_y < 0:
            for i in range(abs(dist_y)):
                grid_data[front_x][front_y - i] = "[ ]"

    elif dist_y == 0:
        if dist_x > 0:
            for i in range(dist_x):
                grid_data[front_x + i][front_y] = "[ ]"
        elif dist_x < 0:
            for i in range(abs(dist_x)):
                grid_data[front_x - i][front_y] = "[ ]"

    print_grid(grid_data)

class Ship:
    def __init__(self, ship_name, ship_length):
        self.name = ship_name
        self.length = ship_length
        self.location_front = None
        self.location_back = None
        self.sunk = False

    def __repr__(self):
        return self.name + " " + str(self.length)

    # def set_ship(self):
    #     front_coords = input("Please enter the starting coordinates of your ship: ")
    #     if len(front_coords) == 2:
    #         if ord("A") <= ord(front_coords[0].upper()) <= ord("J"):
    #             self.location_front = front_coords 
    #             try:
    #                 front_y = int(front_coords[1])
    #                 if 0 <= front_y <= 9:
    #                     back_coords = input("Please enter the ending coordinates of your ship: ")
    #                     if len(back_coords) == 2:
    #                         if ord("A") <= ord(back_coords[0].upper()) <= ord("J"):
    #                             back_x = back_coords[0]
    #                             self.location_back = back_coords
    #                             try:
    #                                 back_y = int(back_coords[1])    
    #                                 if 0 <= back_y <= 9:
    #                                     front_x = front_coords[0]
    #                                     if (ord(front_x) + (self.length - 1)) == ord(back_x) and (front_y == back_y):
    #                                         print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
    #                                     elif (ord(front_x) - (self.length - 1)) == ord(back_x) and (front_y == back_y):
    #                                         print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
    #                                     elif (front_y + (self.length - 1)) == back_y and (front_x == back_x):
    #                                         print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
    #                                     elif (front_y - (self.length - 1)) == back_y and (front_x == back_x):
    #                                         print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
    #                                     else:
    #                                         print("Out of range")
    #                                         self.set_ship()
    #                                     print(self.name + " set at [" + front_coords + ", " + back_coords + "].")
    #                                 else:
    #                                     print("**Must enter an integer between 0 and 9 as the second coordinate character.**")
    #                                     self.set_ship()
    #                             except ValueError:
    #                                 print("**Must enter an integer as the second coordinate character.**")
    #                                 self.set_ship()
    #                         else:
    #                             print("**Must enter a letter between A and J as the first coordinate character.**")
    #                             self.set_ship()
    #                     else:
    #                         print("**Must enter a coordinate that is two characters in length.**")
    #                         self.set_ship()
    #                 else:
    #                     print("**Must enter an integer between 0 and 9 as the second coordinate character.**")
    #                     self.set_ship()
    #             except ValueError:
    #                 print("**Must enter an integer as the second coordinate character.**")
    #                 self.set_ship()
    #         else:
    #             print("**Must enter a letter between A and J as the first coordinate character.**")
    #             self.set_ship()
    #     else:
    #         print("**Must enter a coordinate that is two characters in length.**")
    #         self.set_ship()

    def set_ship(self):
        while True:
            front_coords = input("Enter the starting coordinates for your " + self.name + ": [")
            if len(front_coords) != 2:
                print("*Must enter a coordinate that is two characters in length.*")
                continue
            if not "A" <= front_coords[0].upper() <= "J":
                print("*Must enter a letter between A and J as the first coordinate character.*")
                continue
            try:
                front_y = int(front_coords[1])
                if not 0 <= front_y <= 9:
                    print("*Must enter an integer between 0 and 9 as the second coordinate character.*")
                    continue
            except ValueError:
                print("*Must enter an integer as the second coordinate character.*")
                continue
            break

        while True:
            back_coords = input("Enter the ending coordinates for your " + self.name + ": [" + front_coords.upper() + ", ")
            if len(back_coords) != 2:
                print("*Must enter a coordinate that is two characters in length.*")
                continue
            if not "A" <= back_coords[0].upper() <= "J":
                print("*Must enter a letter between A and J as the first coordinate character.*")
                continue
            try:
                back_y = int(back_coords[1])
                if not 0 <= back_y <= 9:
                    print("*Must enter an integer between 0 and 9 as the second coordinate character.*")
                    continue
            except ValueError:
                print("*Must enter an integer as the second coordinate character.*")
                continue

            front_x = front_coords[0].upper()
            back_x = back_coords[0].upper()
            if (ord(front_x) + (self.length - 1)) == ord(back_x) and (front_y == back_y):
                print(self.name + " set at [" + front_coords.upper() + ", " + back_coords.upper() + "].")
                self.location_front = front_coords.upper()
                self.location_back = back_coords.upper()
                break
            elif (ord(front_x) - (self.length - 1)) == ord(back_x) and (front_y == back_y):
                print(self.name + " set at [" + front_coords.upper() + ", " + back_coords.upper() + "].")
                self.location_front = front_coords.upper()
                self.location_back = back_coords.upper()
                break
            elif (front_y + (self.length - 1)) == back_y and (front_x == back_x):
                print(self.name + " set at [" + front_coords.upper() + ", " + back_coords.upper() + "].")
                self.location_front = front_coords.upper()
                self.location_back = back_coords.upper()
                break
            elif (front_y - (self.length - 1)) == back_y and (front_x == back_x):
                print(self.name + " set at [" + front_coords.upper() + ", " + back_coords.upper() + "].")
                self.location_front = front_coords.upper()
                self.location_back = back_coords.upper()
                break
            else:
                print("Entered coordinates are not within ships range. Please try again.")

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
    def __init__(self, name, ships, grid):
        self.name = name.capitalize()
        self.ships = ships
        self.grid = grid
        self.available_ships = {}
        self.placed_ships = None

        index = 1
        for ship in self.ships:
            self.available_ships[index] = ship
            index += 1      

    def select_ship(self):    
        print(self.available_ships)
        while True:
            try:
                selected_ship = int(input("Please enter a value between 1-5 to select a ship and enter its coordinates: "))
                if selected_ship not in range(1,6):
                    continue
                if selected_ship not in self.available_ships:
                    continue
                return self.available_ships.pop(selected_ship)
            except ValueError:
                continue

#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name, player1_ships, new_grid_data())
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name, player2_ships, new_grid_data())
print("\n")

#Define a game of head or tails.
def coin_flip():

    #Player to select heads or tails is also selected at random, adding another level of probability.
    players = [player1, player2]
    random_player = random.choice(players)

    #Selected player is asked to select head or tails from a terminal input.
    players_choice = input(random_player.name + " please select HEADS or TAILS: ")
    print(random_player.name + " you selected " + players_choice + ".\n")

    #Randomly select heads or tails.
    heads_tails = ["HEADS", "TAILS"]
    result = random.choice(heads_tails)

    #Print the winning result and return winner and loser.
    if result == players_choice.upper():
        print("The coin landed on " + result + "!")
        winner = random_player
        players.remove(random_player)
        loser = players[0]
    else:
        print("The coin landed on " + result + "!")
        loser = random_player
        players.remove(random_player)
        winner = players[0]
    return winner, loser 

#Coin flip between players determines who goes first. Redefine player 1 and player 2 objects based on winner and loser of coin flip.
print("Time to determine who goes first.")
player1, player2 = coin_flip()
print(player1.name + " goes first.")

#Coin flip winner places ships first and will have the first turn.
print_grid(player1.grid)
print(player1.name + " time to place your ships.")
selected_ship = (player1.select_ship())
selected_ship.set_ship()
add_ship_to_grid(selected_ship, player1.grid)

# while len(player1.available_ships) > 0:
#     selected_ship = (player1.select_ship())
#     selected_ship.set_ship()
    
# for ship in player1.ships:
#     print(ship.name + ": is located at [" + ship.location_front + ", " + ship.location_back + "]")