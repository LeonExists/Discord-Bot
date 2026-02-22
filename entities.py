class Entity:
    def __init__(self, icon, x, y):
        self.icon = icon
        self.x = x
        self.y = y

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(":smiley:", x, y)

class Box(Entity):
    def __init__(self, x, y):
        super().__init__(":orange_square:", x, y)

class Goal(Entity):
    def __init__(self, x, y):
        super().__init__(":green_square:", x, y)

