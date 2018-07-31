""" 
This is the addition of a generic entity class to represent players, enemies, items, etc... 
entity.py
"""

class Entity:
    # Defining properties of the Entity class
    def __init__(self, x, y, char, color, name, blocks=False): 
        self.x = x
        self.y = y
        self.char = char # '@' symbol for player
        self.color = color # 'white' for player by default
        self.name = name
        self.blocks = blocks

    # defining  method 'move' to move the entity by a given amount
    def move(self, dx, dy): 
        self.x += dx
        self.y += dy

def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity

    return None