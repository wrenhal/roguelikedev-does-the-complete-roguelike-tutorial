# This will be my working main file for the RogueLike tutorial
# Renaming to engine.py to follow http://rogueliketutorials.com/libtcod/1

import libtcodpy as libtcod # Imports the Graphics library
# Now adding import of the handle_keys() function
from input_handlers import handle_keys
# Now adding Entity support from entity.py
from entity import Entity
# Adding support for render functions from render_functions.py
from render_functions import clear_all, render_all
# Now importing logic for creating the game map.
from map_objects.game_map import GameMap
# Import the FOV functions
from fov_functions import initialize_fov, recompute_fov


def main(): # Adding the main function for Python 3 compatibility

# Setting constants and global variables
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10
    brown_color = libtcod.flame * libtcod.light_blue
    colors = {
        'dark_wall': brown_color, # Color(0, 0, 100),
        'dark_ground': libtcod.desaturated_orange, # Color(50, 50, 150)
        'light_wall': libtcod.dark_flame,
        'light_ground': libtcod.light_orange
    } # Coloring our tiles
    # LIMIT_FPS = 20 # Unused for now
    """
    Setting player coordinate starting point at center of console
    and setting an NPC character now
    """
    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

# Initializing the library font
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# Now creating the window with size constants, title, and whether fullscreen
    libtcod.console_init_root(screen_width, screen_height, 'python/libtcod tutorial', False)
    con = libtcod.console_new(screen_width, screen_height) # Allows the ability to create new consoles
    game_map = GameMap(map_width, map_height) # Initialize the game map
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    fov_recompute = True # Whether to reset the Field of View, True for start of game
    fov_map = initialize_fov(game_map) #Initialize the Field of View
    key = libtcod.Key()  # Setting keyboard variable for input
    mouse = libtcod.Mouse() # Setting mouse variable for input
    
# Next is the main game loop.  We basically print the @ character to the screen in white
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        #libtcod.console_set_default_foreground(0, libtcod.white) 
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
# Changing the way the console is initialized so we can reference different consoles later
# Removed the previous calls because render logic is now in render_functions.py
        # render_all(con, entities, game_map, screen_width, screen_height, colors)
        render_all(con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors)

        fov_recompute = False

        libtcod.console_flush() # Flush the console which writes any changes to the screen
        
        clear_all(con, entities)

# New setup to call handle_keys() function from input_handlers.py
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            # player_x += dx
            # player_y += dy
            # player.move(dx, dy) updating player.move logic
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
                fov_recompute = True # Recompute the FOV upon movement

        if exit:
                return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)

if __name__ == '__main__': # Declare the main function to be called
     main()