class Army:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        # move the army by dx, dy steps
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"{self.name} ({self.x}, {self.y})"
    