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

if __name__ == "__main__":
    test_map = WorldMap(10, 10)
    test_map.display()
