
class Army:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.current_terrain = ' ' #assuming starting on neutral ground

    def move(self, dx, dy, currentMap):
        #place old terrain symbol before moving
        currentMap.grid[self.x][self.y] = self.current_terrain
                
        # move the army by dx, dy steps
        self.x += dx
        self.y += dy

        self.current_terrain = currentMap.grid[self.x][self.y]
        currentMap.grid[self.x][self.y] = self

    def __repr__(self):
        return f"{self.name} ({self.x}, {self.y})"
    
    def symbol(self):
        return "X"
    