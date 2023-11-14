import random
import os

from tribes.army import Army

#these are standalone functions to replace the class methods
#this will be a module that hosues standalone functions, and does not have a class or object for now.

def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # Assume it's Unix/Linux/MacOS
        os.system('clear')

def printArmyStatus(inputArmy):
    print("The army called the " + inputArmy.name + " is at x: " + str(inputArmy.x) + ", y: " + str(inputArmy.y))

def updateyMap(inputMap):
    clear_screen()
    for y in range(inputMap.height):
        row_display = []
        for x in range(inputMap.width):
            try:
                cell = inputMap.grid[y][x]  # Accessing cell at coordinates (x, y)
                cell_display = '[{}]'.format(cell.symbol() if isinstance(cell, Army) else cell)
                row_display.append(cell_display)
            except IndexError:
                print(f"IndexError at x={x},y={y}")
                raise
        print(''.join(row_display))

def get_user_interaction(interaction_type, **context):
    #Handles different types of user interactions based on the specified interaction type.

    #:param interaction_type: The type of interaction (e.g., 'enter_command', 'move_army').
    #:param context: Optional contextual information for specific interactions.
    #:return: User input or other interaction output.

    #current functions include
    #'input_command'
    #'move_army'
    #'quit'
    while True:
        if interaction_type == 'input_command':
            user_input = input("Please enter a command: (move/quit)")
        # Additional cases can be added here as the game develops
        else:
            raise ValueError("Unknown interaction type")

        if user_input.lower().strip() == "quit":
            confirm_quit = input("Are you sure you want to quit? (yes/no): ").lower().strip()
            if confirm_quit == "yes":
                return "quit"
            else:
                continue  # Go back to asking for input
        return user_input











"""
            user_input = input("Please enter your command: ")
            if user_input == "quit":
                break #exit game loop
            if user_input.startswith("move"):
                _, direction = user_input.split()
                dx, dy = 0, 0
                if direction == "up":
                    dy = -1
                elif direction == "down":
                    dy = 1
                elif direction == "left":
                    dx = -1
                elif direction == "right":
                    dx = 1
                game_map.move_army(player_army, dx, dy)
        except ValueError as e:
            print(e)
            print("Resetting, in...")
            for i in range(3):
                time.sleep(1)
                print(3-i)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")
"""