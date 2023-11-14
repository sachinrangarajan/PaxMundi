import os
import time

from map.world_map import WorldMap
from tribes.army import Army
from ui import uiUtils

def main():
    """Main game loop."""
    #create an instance of the WorldMap Class with the desired dimensions
    game_map = WorldMap(15, 15)

 # Create an army for testing
    player_army = Army("Red Brigade", 0, 0)
    game_map.add_army(player_army)

    while True:
        try:
            uiUtils.updateyMap(game_map)
            uiUtils.printArmyStatus(player_army)
            user_input = uiUtils.get_user_interaction('input_command')
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
                else:
                    raise ValueError(f"Unknown direction: {direction}")
                game_map.move_army(player_army, dx, dy)

        except ValueError as e:
            print(e)
            print("Resetting, in...")
            for i in range(10):
                time.sleep(0.1)
                print(10-i)
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")

#        uiUtils.displayMap(game_map)

#only run when we execute this code directly, but then again - it should always be executed directly since this is the main file!
if __name__ == "__main__":
    main()
