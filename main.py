import os
from map.world_map import WorldMap
from units.army import Army

def main():
    """Main game loop."""
 # Create an army for testing
    player_army = Army("Red Brigade", 0, 0)
    game_map.add_army(player_army)

    #create an instance of the WorldMap Class with the desired imensions
    game_map = WorldMap(11, 11)

    while True:
        os.system('cls')
        game_map.display()

        user_input = input("Enter your command: ")
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

        # ... (rest of your game loop)



        #here we would handle command for muving units etc.






        #placeholder to update change game state
        # game_map.update()

#only run when we execute this code directly, but then again - it should always be executed directly since this is the main file!
if __name__ == "__main__":
    main()
