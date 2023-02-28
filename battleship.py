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
    for row in grid_data:
        print_row = ""
        for col in row:
            add_col = col
            print_row += add_col
        print(print_row)

class Ship:
    def __init__(self, ship_name, ship_length):
        self.name = ship_name
        self.length = ship_length
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
                    if front_y == 0:
                        front_y = 10
                        front_coords = chr(front_x) + str(front_y)

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
                        if back_y == 0:
                            back_y = 10
                            back_coords = chr(back_x) + str(back_y)

                    except ValueError: #Catch error if second character is not an integer.
                        print("*Must enter an integer as the second coordinate character.*")
                        continue

                    dist_x = back_x - front_x
                    dist_y = back_y - front_y

                    if back_coords in player.all_ship_coords: #Check if entered coordinate has already been assigned to another ship.
                        print("The entered coordinate is already occupied by another ship! Try again!")
                        continue

                    if dist_x == 0 and (front_y + (self.length - 1)) == back_y: #Horizontal (L to R)
                        break
                    elif dist_x == 0 and (front_y - (self.length - 1)) == back_y: #Horizontal (R to L)
                        break
                    elif dist_y == 0 and (front_x + (self.length - 1)) == back_x: #Vertical (Top to Bottom)
                        break
                    elif dist_y == 0 and (front_x - (self.length - 1)) == back_x: #Vertical (Bottom to Top)
                        break
                    else:
                        print("Entered coordinates are not within ships range. Please try again! Ships length: " + str(self.length))
                        continue

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

                for coord in new_coords:
                    if coord in player.all_ship_coords:
                        placed_successfully = False
                    else:
                        continue

                if all(coord not in player.all_ship_coords for coord in new_coords):
                    self.all_coords.extend(new_coords)
                    player.all_ship_coords.extend(new_coords)
                    placed_successfully = True
                    print(self.all_coords)
                    print(player.all_ship_coords)

                break

        for coord in self.all_coords:
            player.grid[(ord(coord[0]) - 64)][int(coord[1:])] = "[ ]"

    def reset(self, player):
        print("Resetting " + self.name + "...")
        try:
            for coord in self.all_coords:
                player.grid[ord(coord[0]) - 64][int(coord[1:])] = " - "
                player.all_ship_coords.remove(coord)
            self.all_coords = []
            self.place_ship(player)
        except ValueError:
            pass

class Player:
    def __init__(self, name, ships):
        self.name = name.capitalize()
        self.ships = ships

        self.grid = new_grid_data()
        self.grid_shots = new_grid_data()

        self.available_ships = {}
        self.all_ship_coords = []
        self.shots_fired = []
        self.hits = []

        index = 1
        for ship in self.ships:
            self.available_ships[index] = ship
            index += 1      

    def __repr__(self):
        return self.name

    def setup(self):
        print(self.name + " time to place your ships.")
        while len(self.available_ships) > 0:
            print_grid(self.grid)
            selected_ship = (self.select_ship())
            selected_ship.place_ship(self)
        self.print_confirm()

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

    def fire(self, opponent):

        print_grid(self.grid_shots)
        
        while True: #Loop until coordinate is entered in the correct format.

            #User inputs coordinate with auto-capitalization.
            shot_coord = input(self.name + " please enter a coordinate: ").upper()

            if len(shot_coord) != 2: #Check if input is two characters long.
                print("*Must enter a coordinate that is two characters in length.*")
                continue
            if not "A" <= shot_coord[0] <= "J": #Check if first character is between A-J.
                print("*Must enter a letter between A and J as the first coordinate character.*")
                continue

            try: #Check if second character is an integer.
                shot_x = ord(shot_coord[0])
                shot_y = int(shot_coord[1])
                if not 0 <= shot_y <= 9: #Check if second character is between 0-9.
                    print("*Must enter an integer between 0 and 9 as the second coordinate character.*")
                    continue
                if shot_y == 0:
                    shot_y = 10
                    shot_coord = chr(shot_x) + str(shot_y)
            except ValueError: #Catch error if second character is not an integer.
                print("*Must enter an integer as the second coordinate character.*")
                continue

            if shot_coord in self.shots_fired:
                print("You have already fired this shot. Please enter a different coordinate.")
                continue
            
            self.shots_fired.append(shot_coord)

            if shot_coord in opponent.all_ship_coords: #Check if entered coordinate is in the opponent's all_ship_coords.
                print("HIT!")
                opponent.all_ship_coords.remove(shot_coord)
                self.grid_shots[shot_x - 64][shot_y] = "[X]"
            else:
                print("MISS.")
                self.grid_shots[shot_x - 64][shot_y] = " 0 "

            break

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
        winner = random_player
        players.remove(random_player)
        loser = players[0]
    else:
        loser = random_player
        players.remove(random_player)
        winner = players[0]
    print("The coin landed on " + result + "!")
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
player1 = Player(player1_name, player1_ships)
player2_name = input("Please enter the name of player 2: ")
player2 = Player(player2_name, player2_ships)

print("\nTime to determine who goes first.")
player1, player2 = coin_flip()
print(player1.name + " goes first.")

player1.setup()
player2.setup()

print("Both player's ships have been placed. Prepare for battle!")

while len(player1.all_ship_coords) > 0 and len(player2.all_ship_coords) > 0:

    player1.fire(player2)
    if len(player2.all_ship_coords) == 0:
        print(player1.name + " is the winner!")
        break

    player2.fire(player1)
    if len(player1.all_ship_coords) == 0:
        print(player2.name + " is the winner!")
        break