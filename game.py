# Entites
from entities import *

# example level
level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 3, 0, 4, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 0 = empty, 1 = wall, 2 = player, 3 = box, 4 = goal

game_mapping = {
    0 : ":black_large_square:",
    1 : ":red_square:",
    2 : Player(0, 0),
    3 : Box(0, 0),
    4 : Goal(0, 0)
}



class Game:
    def __init__(self, msg):
        # discord utility
        self.msg = msg

        # game
        self.output = [[]]

        self.map = [[]]
        self.entities = []
        self.create_game()


    def create_game(self):
        # create map from level
        self.create_map()

        # create entities from level
        self.create_entities()

    def create_map(self):
        # get raw level
        self.map = level

        # remove entities from map
        self.map = [[0 if cell in [2, 3, 4] else cell for cell in row] for row in self.map]
        
        print(f"Map: \n {self.map}")

    def create_entities(self):
        for row_idx, row in enumerate(level):
            for col_idx, cell in enumerate(row):
                if cell > 1:
                    entity = game_mapping[cell]
                    entity.x = col_idx
                    entity.y = row_idx
                    self.entities.append(entity)

        print(f"Entities: \n {self.entities}")


    def render(self):
        # render map
        self.output = [[game_mapping[cell] for cell in row] for row in self.map]

        print(f"Render, 1: \n {self.output}")

        # render entities
        for entity in self.entities:
            self.output[entity.y][entity.x] = entity.icon

        print(f"Render, 2: \n {self.output}")