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
    
    
    def add_army(self, army):
        self.grid[army.x][army.y] = army
        # Place an army on the map at its coordinates. assumes coordinates are valid.

    def move_army(self, army, dx, dy):
        # Calculate new position
        new_x = army.x + dx
        new_y = army.y + dy
        # Check if the new position is within the map boundaries
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            army.move(dx, dy, self)
        else:
            print("That position is off the map!")
            raise ValueError("tried to do some out of bounds shenanigans")
    
if __name__ == "__main__": #this ensures that it only runs if it is executed directly, not as a module!
    test_map = WorldMap(2, 2)
    test_map.display()
