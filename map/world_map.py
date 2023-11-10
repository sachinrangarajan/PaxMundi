from 

class WorldMap:
    def __init__(self, width, height):
        #initialize the map with the given dimensions
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    
    def display(self):
        #temporary method to visualize the map in the console
        for row in self.grid:
            print(" " .join(["[ ]" if cell is None else "[X]" for cell in row]))
    
    #add more here to manage map

    def add_army(self, army):
        # Place an army on the map at its coordinates
        if (0 <= army.x < self.width) and (0 <= army.y < self.height):
            self.grid[army.y][army.x] = army
        else:
            print("That position is off the map!")

    def move_army(self, army, dx, dy):
        # Move an army to a new location on the map
        # First, remove the army from its current location
        self.grid[army.y][army.x] = None

        # Update the army's position
        army.move(dx, dy)

        # Place the army at the new location
        self.add_army(army)
    





if __name__ == "__main__": #this ensures that it only runs if it is executed directly, not as a module!
    test_map = WorldMap(2, 2)
    test_map.display()
