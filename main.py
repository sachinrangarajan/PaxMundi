import os

from map.world_map import WorldMap

def main():
    """Main game loop."""

    #create an instance of the WorldMap Class with the desired imensions
    game_map = WorldMap(11, 11)

    while True:
        os.system('cls')
        game_map.display()

        user_input = input("Enter your command: ")
        if user_input == "quit":
            break #exit game loop

        #here we would handle command for muving units etc.

        #placeholder to update change game state
        # game_map.update()

#only run when we execute this code directly, but then again - it should always be executed directly since this is the main file!
if __name__ == "__main__":
    main()