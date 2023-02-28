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

            print("Starting placed_successfully loop.")

            #Loop until first coordinate is enterd in the correct format.
            while True:

                print("Starting enter first coordinate loop.")

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

                    print("Starting enter second coordinate loop.")

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

                print(front_x, front_y, back_x, back_y)
                print("Starting to find all coords for ship.")

                new_coords = []

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
                print("Starting coordinate check.")

                for coord in new_coords:
                    if coord in player.all_ship_coords:
                        print("Coordinate [" + coord + "] already occupied by another ship! Try again!")
                        placed_successfully = False
                    else:
                        print("Coordinate [" + coord + "] not found in all_ship_coords.")
                        continue

                if all(coord not in player.all_ship_coords for coord in new_coords):
                    self.all_coords.extend(new_coords)
                    print(player.all_ship_coords)
                    print("Set ship coordinates to all ship coordinates.")
                    player.all_ship_coords.extend(new_coords)
                    print(player.all_ship_coords)
                    placed_successfully = True

                print("End coordinate check.")
                print(self.all_coords)
                print(player.all_ship_coords)
                
                break

        print("Out of placed_successfully loop.")

        print("Adding " + self.name + " to grid.")
        print(front_x, front_y, back_x, back_y)

        player.grid[front_x - 64][front_y] = "[ ]"
        player.grid[back_x - 64][back_y] = "[ ]"
        
        if dist_x == 0: #Horizontal
            if dist_y > 0: #L to R
                for i in range(dist_y):
                    player.grid[front_x - 64][front_y + i] = "[ ]"
            elif dist_y < 0: #R to L
                for i in range(abs(dist_y)):
                    player.grid[front_x - 64][front_y - i] = "[ ]"

        elif dist_y == 0: #Vertical
            if dist_x > 0: #Top to Bottom
                for i in range(dist_x):
                    player.grid[(front_x - 64) + i][front_y] = "[ ]"
            elif dist_x < 0: #Bottom to Top
                for i in range(abs(dist_x)):
                    player.grid[(front_x - 64) - i][front_y] = "[ ]"

        print(front_x, front_y, back_x, back_y)
        print(self.name + " added to grid.")
        print_grid(player.grid)
            
        #Check if the entered coordinates are on the same row/column and of equal distance to the length of the ship being entered.
        if dist_x == 0 and (front_y + (self.length - 1)) == back_y: #Horizontal (L to R)
            self.location_front = front_coords
            self.location_back = back_coords
            print(self.name + " set at [" + front_coords + ", " + back_coords + "]." + " (L to R)")

        elif dist_x == 0 and (front_y - (self.length - 1)) == back_y: #Horizontal (R to L)
            self.location_front = front_coords
            self.location_back = back_coords
            print(self.name + " set at [" + front_coords + ", " + back_coords + "]." + " (R to L)")

        elif dist_y == 0 and (front_x + (self.length - 1)) == back_x: #Vertical (Top to Bottom)
            self.location_front = front_coords
            self.location_back = back_coords
            print(self.name + " set at [" + front_coords + ", " + back_coords + "]." + " (Top to Bottom)")

        elif dist_y == 0 and (front_x - (self.length - 1)) == back_x: #Vertical (Bottom to Top)
            self.location_front = front_coords
            self.location_back = back_coords
            print(self.name + " set at [" + front_coords + ", " + back_coords + "]." + " (Bottom to Top)")

        else:
            print("Entered coordinates are not within ships range. Please try again.")

    def reset(self, player):
        print("Relocating " + self.name + "...")
        try:
            for coord in self.all_coords:
                coord_x = ord(coord[0]) - 64
                coord_y = int(coord[1])
                if len(coord) == 3 and coord_y == 1 and int(coord[2]) == 0:
                    coord_y = int(coord[1:])
                print("Removing coordinate [" + coord + "] from " + player.name + "'s grid.")
                player.grid[coord_x][coord_y] = " - "
                player.all_ship_coords.remove(coord)
        except ValueError:
            pass
        self.location_front = None
        self.location_back = None
        self.all_coords = []
        self.place_ship(player)

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
print_grid(player1.grid)
print(player1.name + " time to place your ships.")

# selected_ship = (player1.select_ship())
# selected_ship.place_ship(player1)
# selected_ship = (player1.select_ship())
# selected_ship.place_ship(player1)

while len(player1.available_ships) > 0:
    selected_ship = (player1.select_ship())
    selected_ship.place_ship(player1)
    
# for ship in player1.ships:
#     print(ship.name + ": is located at [" + ship.location_front + ", " + ship.location_back + "]")

# print(player1.all_ship_coords)