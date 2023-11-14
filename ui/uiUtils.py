import random
import os


from tribes.army import Army

#these are standalone functions to replace the class methods

def generate_random_map(width, height):
    """
    Generate a random map.

    :param width: Width of the map.
    :param height: Height of the map.
    :return: Generated map as a 2D list.
    """
    terrain = ['M', 'W', 'T', ' ']  # M: Mountain, W: Water, T: Forest, ' ': Neutral
    return [[random.choice(terrain) for _ in range(width)] for _ in range(height)]

def clear_screen():
    """
    Clears the terminal screen.
    """
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # Assume it's Unix/Linux/MacOS
        os.system('clear')

def armyStatus(inputArmy):
    print("The army, called the" + inputArmy.name + ", is at x: " + str(inputArmy.x) + ", y: " + str(inputArmy.y))

def get_user_interaction(interaction_type, **context):
    """
    Handles different types of user interactions based on the specified interaction type.

    :param interaction_type: The type of interaction (e.g., 'enter_command', 'move_army').
    :param context: Optional contextual information for specific interactions.
    :return: User input or other interaction output.
    """
    while True:
        if interaction_type == 'enter_command':
            user_input = input("Enter a command: ")
        elif interaction_type == 'move_army':
            army_name = context.get('army_name', 'Unknown Army')
            user_input = input(f"Please input the direction you want {army_name} to move: ")
        # Additional cases can be added here as the game develops
        else:
            raise ValueError("Unknown interaction type")

        if user_input.lower().strip() == "quit":
            confirm_quit = input("Are you sure you want to quit? (yes/no): ").lower().strip()
            if confirm_quit == "yes":
                return "quit"
            else:
                continue  # Go back to asking for input
        else:
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
            

class uiUtils:
    def __init__(self):
        #first figure out if we are using a mac or a pc


        return

    def generate_random_map(self):
        # Creation Myth: In the beginning, the world was a blank canvas...with trumpets and horns of Purcell hearlding a new day
        terrain = ['M', 'W', 'T', ' ']  # M: Mountain, W: Water, T: Forest, ' ': Neutral
        return [[random.choice(terrain) for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        for y in range(self.height):
            row_display = []
            for x in range(self.width):
                try:
                    cell = self.grid[x][y]  # Accessing cell at coordinates (x, y)
                    cell_display = '[{}]'.format(cell.symbol() if isinstance(cell, Army) else cell)
                    row_display.append(cell_display)
                except IndexError:
                    print(f"IndexError at x={x},y={y}")
                    raise
            print(' '.join(row_display))

    #add more here to manage map
    