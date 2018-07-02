from map_objects.tile import Tile
# setting up the GameMap class to be called from engine.py

class GameMap: # Now definine the class and it's properties
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self): 
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]
        # Creating a 2d array tiles to fill the map and a series of blocked tiles.
        tiles[30][22].blocked = True
        tiles[30][22].block_sight = True
        tiles[31][22].blocked = True
        tiles[31][22].block_sight = True
        tiles[32][22].blocked = True
        tiles[32][22].block_sight = True

        return tiles

    # Method to determine if tile is blocked.
    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False