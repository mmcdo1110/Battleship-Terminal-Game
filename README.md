# Battleship-Terminal-Game

Final project for python3 section of Computer Science 101 course path on Codecademy.

This game of battleship takes in the names of two players and decides who goes first through a game of heads or tails. The winner selects from a list of their available ships and places each one using the front and back coordinates. The program loops until the coordinates are given in the correct format, have a distance equal to the length of the selected ship, and are not already occupied by another. The player’s grid is updated and printed with the newly placed ship, prompts another selection, and repeats. After, the player is asked to confirm or relocate the original placements. If the player chooses to relocate a ship, the grid is updated accordingly, and the confirmation process repeats until all ships have been confirmed. The opposing player then follows the same procedures for setting up their fleet. 

On each turn, a player is asked to select an enemy coordinate to fire upon, confirm that coordinate, and fire on command. A new grid is printed for the player with no ships displayed but informs the player of the results, marking an “X” for a hit or an “O” for a miss, along with a move description. Once all a player’s ships have been destroyed, the game is over, and the survivor is crowned the winner.
