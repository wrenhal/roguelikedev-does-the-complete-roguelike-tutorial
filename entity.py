""" 
This is the addition of a generic entity class to represent players, enemies, items, etc... 
entity.py
"""

class Entity:
    # Defining properties of the Entity class
    def __init__(self, x, y, char, color): 
        self.x = x
        self.y = y
        self.char = char # '@' symbol for player
        self.color = color # 'white' for player by default

    # defining  method 'move' to move the entity by a given amount
    def move(self, dx, dy): 
        self.x += dx
        self.y += dy
        