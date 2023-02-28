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

class Ship:
    def __init__(self, ship_name, ship_length):
        self.name = ship_name
        self.length = ship_length
        self.location_front = None
        self.location_back = None
        self.all_coords = []
        self.sunk = False

    def __repr__(self):
        return self.name + " " + str(self.length)

    def place_ship(self, player):

        placed_successfully = False
        while not placed_successfully:

            #Loop until first coordinate is enterd in the correct format.
            while True:

                #User inputs first coordinate with auto-capitalization.
                front_coords = input("Enter the starting coordinates for your " + self.name + ": [").upper()
                if len(front_coords) != 2: #Check if input is two characters long.
                    print("*Must enter a coordinate that is two characters in length.*")
                    continue
                if not "A" <= front_coords[0] <= "J": #Check if first character is between A-J.
                    print("*Must enter a letter between A and J as the first coordinate character.*")
                    continue
                try: #Check if second character is an integer.

                    front_x = ord(front_coords[0])
                    front_y = int(front_coords[1])

                    if not 0 <= front_y <= 9: #Check if second character is between 0-9.
                        print("*Must enter an integer between 0 and 9 as the second coordinate character.*")
                        continue
                except ValueError: #Catch error if second character is not an integer.
                    print("*Must enter an integer as the second coordinate character.*")
                    continue
                if front_coords in player.all_ship_coords: #Check if entered coordinate has already been assigned to another ship.
                        print("The entered coordinate is already occupied by another ship! Try again!")
                        continue

                    #Loop until second coordinate is entered in the correct format.
                while True:

                    #User inputs second coordinate with auto-capitalization. Displays first coordinate before input.
                    back_coords = input("Enter the ending coordinates for your " + self.name + ": [" + front_coords.upper() + ", ").upper()
                    if len(back_coords) != 2: #Ceck if input is two characters long.
                        print("*Must enter a coordinate that is two characters in length.*")
                        continue
                    if not "A" <= back_coords[0] <= "J": #Check if first character is between A-J.
                        print("*Must enter a letter between A and J as the first coordinate character.*")
                        continue
                    try: #Check if second character is an integer.

                        back_x = ord(back_coords[0])
                        back_y = int(back_coords[1])

                        if not 0 <= back_y <= 9: #Check if second character is between 0-9.
                            print("*Must enter an integer between 0 and 9 as the second coordinate character.*")
                            continue
                    except ValueError: #Catch error if second character is not an integer.
                        print("*Must enter an integer as the second coordinate character.*")
                        continue

                    if back_coords in player.all_ship_coords: #Check if entered coordinate has already been assigned to another ship.
                        print("The entered coordinate is already occupied by another ship! Try again!")
                        continue
                    break

                if front_y == 0:
                    front_y = 10
                if back_y == 0:
                    back_y = 10

                dist_x = back_x - front_x
                dist_y = back_y - front_y
                new_coords = []

                print("Starting to find all coords for ship.")

                if dist_x == 0: #Horizontal
                    if dist_y > 0: #Left => Right
                        for i in range(self.length):
                            new_coord = chr(front_x) + str(front_y + i)
                            new_coords.append(new_coord)
                    elif dist_y < 0: #Right => Left
                        for i in range(self.length):
                            new_coord = chr(front_x) + str(back_y + i)
                            new_coords.append(new_coord)
                elif dist_y == 0: #Vertical
                    if dist_x > 0: #Top => Bottom
                        for i in range(self.length):
                            new_coord = chr(front_x + i) + str(front_y)
                            new_coords.append(new_coord)
                    elif dist_x < 0: #Bottom => Top
                        for i in range (self.length):
                            new_coord = chr(back_x + i) + str(front_y)
                            new_coords.append(new_coord)    

                print("Found all coordinates. Your new coords are:", new_coords)

                for coord in new_coords:
                    if coord in player.all_ship_coords:
                        print("Coordinate [" + coord + "] already occupied by another ship! Try again!")
                        placed_successfully = False
                    else:
                        print("Coordinate [" + coord + "] not found in all_ship_coords.")
                        continue

                if all(coord not in player.all_ship_coords for coord in new_coords):
                    self.all_coords.extend(new_coords)
                    player.all_ship_coords.extend(new_coords)
                    placed_successfully = True
                    print(self.all_coords)
                    print(player.all_ship_coords)

                break

        print("Adding " + self.name + " to grid.")

        for coord in self.all_coords:
            if len(coord) == 3:
                player.grid[(ord(coord[0]) - 64)][int(coord[1:])] = "[ ]"
            else:
                player.grid[(ord(coord[0]) - 64)][int(coord[1])] = "[ ]"
                
        print(self.name + " added to grid.")
        print(self.name + " set at [" + front_coords + ", " + back_coords + "]." + " (Bottom to Top)")
        print_grid(player.grid)
            
        # #Check if the entered coordinates are on the same row/column and of equal distance to the length of the ship being entered.
        # if dist_x == 0 and (front_y + (self.length - 1)) == back_y: #Horizontal (L to R)

        # elif dist_x == 0 and (front_y - (self.length - 1)) == back_y: #Horizontal (R to L)

        # elif dist_y == 0 and (front_x + (self.length - 1)) == back_x: #Vertical (Top to Bottom)

        # elif dist_y == 0 and (front_x - (self.length - 1)) == back_x: #Vertical (Bottom to Top)
            
        # else:
        #     print("Entered coordinates are not within ships range. Please try again.")

    def reset(self, player):
        print("Relocating " + self.name + "...")
        try:
            for coord in self.all_coords:
                print("Removing coordinate [" + coord + "] from " + player.name + "'s grid.")
                if len(coord) == 3:
                    player.grid[ord(coord[0]) - 64][int(coord[1:])] = " - "
                player.grid[ord(coord[0]) - 64][int(coord[1])] = " - "
                player.all_ship_coords.remove(coord)
            self.all_coords = []
            self.place_ship(player)
        except ValueError:
            pass

class Player:
    def __init__(self, name, ships, grid):
        self.name = name.capitalize()
        self.ships = ships
        self.grid = grid
        self.available_ships = {}
        self.placed_ships = None
        self.all_ship_coords = []

        index = 1
        for ship in self.ships:
            self.available_ships[index] = ship
            index += 1      

    def __repr__(self):
        return self.name

    def select_ship(self):    
        print(list(self.available_ships.items()))
        while True:
            try:
                selected_ship = int(input("Please enter a value {} to select a ship and enter its coordinates: ".format(list(self.available_ships.keys()))))
                if selected_ship not in range(1,6):
                    continue
                if selected_ship not in self.available_ships:
                    continue
                return self.available_ships.pop(selected_ship)
            except ValueError:
                continue

    def print_confirm(self):    
        for ship in self.ships:
            print(ship.name + ": is located at ", ship.all_coords)
            player_choice = str(input("Confirm placement? (Y/N): ").upper())
            if player_choice == "Y":
                continue
            elif player_choice == "N":
                ship.reset(self)

    def fire(self):
        pass

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

#Define player 1 and 2 names through terminal inputs.
player1_name = input("Please enter the name of player 1: ")
player1 = Player(player1_name, player1_ships, new_grid_data())
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name, player2_ships, new_grid_data())
print("\n")

#Coin flip between players determines who goes first. Redefine player 1 and player 2 objects based on winner and loser of coin flip.
print("Time to determine who goes first.")
player1, player2 = coin_flip()
print(player1.name + " goes first.")

#Coin flip winner places ships first and will have the first turn.
print_grid(new_grid_data())

print(player1.name + " time to place your ships.")

while len(player1.available_ships) > 0:
    selected_ship = (player1.select_ship())
    selected_ship.place_ship(player1)

player1.print_confirm()
    
print(player2.name + " time to place your ships.")

while len(player2.available_ships) > 0:
    selected_ship = (player2.select_ship())
    selected_ship.place_ship(player2)

player2.print_confirm()