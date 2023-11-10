import random

from tribes.army import Army
class WorldMap:
    def __init__(self, width, height):
        #initialize the map with the given dimensions
        self.width = width
        self.height = height
        self.grid = self.generate_random_map()

    def generate_random_map(self):
        # Creation Myth: In the beginning, the world was a blank canvas...with trumpets and horns of Purcell hearlding a new day
        terrain = ['M', 'R', 'T', ' ']  # M: Mountain, R: River, T: Forest, ' ': Neutral
        return [[random.choice(terrain) for _ in range(self.width)] for _ in range(self.height)]
    
    def display(self):
    # The Scroll of Sight: Unveiling the hidden lands...
        for row in self.grid:
            print(' '.join(['[{}]'.format(cell) for cell in row]))

    #add more here to manage map
    
    
    def add_army(self, army):
        self.grid[army.y][army.x] = army
        # Place an army on the map at its coordinates. assumes coordinates are valid.

    def move_army(self, army, dx, dy):
        # Calculate new position
        new_x = army.x + dx
        new_y = army.y + dy
        # Check if the new position is within the map boundaries
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            # First, remove the army from its current location
            self.grid[army.y][army.x] = None
            army.move(dx, dy)
            # Place the army at the new location
            self.add_army(army)
        else:
            print("That position is off the map!")
            raise ValueError("tried to do some out of bounds shenanigans")
    
if __name__ == "__main__": #this ensures that it only runs if it is executed directly, not as a module!
    test_map = WorldMap(2, 2)
    test_map.display()
