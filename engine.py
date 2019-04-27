# This will be my working main file for the RogueLike tutorial
# Renaming to engine.py to follow http://rogueliketutorials.com/libtcod/1

# 4/26/2019 Replacing all print statements with calls to the Message_log.add_message function
# and adding code to handle mouse events in preparation for mouse_over events.

import libtcodpy as libtcod # Imports the Graphics library
# Now adding import of the handle_keys() function
from input_handlers import handle_keys
# Now adding Entity support from entity.py
from entity import Entity, get_blocking_entities_at_location
# Adding support for render functions from render_functions.py
from render_functions import clear_all, render_all, RenderOrder
# Now importing logic for creating the game map.
from map_objects.game_map import GameMap
# Import the FOV functions
from fov_functions import initialize_fov, recompute_fov
# import MessageLog function
from game_messages import MessageLog
# Import GameStates enum
from game_states import GameStates
# Import Fighter class
from components.fighter import Fighter
from death_functions import kill_monster, kill_player


def main(): # Adding the main function for Python 3 compatibility

# Setting constants and global variables
    screen_width = 80
    screen_height = 50
    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height
# Adding variables Message log display to show events.
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 80
    map_height = 43
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10
    max_monsters_per_room = 3
    brown_color = libtcod.flame * libtcod.light_blue
    colors = {
        'dark_wall': brown_color, # Color(0, 0, 100),
        'dark_ground': libtcod.desaturated_orange, # Color(50, 50, 150)
        'light_wall': libtcod.dark_flame,
        'light_ground': libtcod.light_orange
    } # Coloring our tiles
    # LIMIT_FPS = 20 # Unused for now
    # Setting player coordinate starting point at center of console
    fighter_component = Fighter(hp=30, defense=2, power=5) # Setting player attributes
    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR, fighter=fighter_component)
    entities = [player]

# Initializing the library font
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# Now creating the window with size constants, title, and whether fullscreen
    libtcod.console_init_root(screen_width, screen_height, 'python/libtcod tutorial', False)
    con = libtcod.console_new(screen_width, screen_height) # Allows the ability to create new consoles
    panel = libtcod.console_new(screen_width, panel_height)  # New console to hold HP and Messages
    game_map = GameMap(map_width, map_height) # Initialize the game map
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities, max_monsters_per_room)
    fov_recompute = True # Whether to reset the Field of View, True for start of game
    fov_map = initialize_fov(game_map) #Initialize the Field of View
    message_log = MessageLog(message_x, message_width, message_height)
    key = libtcod.Key()  # Setting keyboard variable for input
    mouse = libtcod.Mouse() # Setting mouse variable for input
    game_state = GameStates.PLAYERS_TURN # Sets initial game_state to players turn

    
# Next is the main game loop.  We basically print the @ character to the screen in white
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        #libtcod.console_set_default_foreground(0, libtcod.white) 
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)
# Changing the way the console is initialized so we can reference different consoles later

        render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width,
                   screen_height, bar_width, panel_height, panel_y, mouse, colors)

        fov_recompute = False

        libtcod.console_flush() # Flush the console which writes any changes to the screen
        
        clear_all(con, entities)

# New setup to call handle_keys() function from input_handlers.py
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        player_turn_results = [] # new dictionary

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy

            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)

                if target: # Are you running into a monster?
                    attack_results = player.fighter.attack(target) # Attack monster
                    player_turn_results.extend(attack_results) # Get results of attack
                else:
                    player.move(dx, dy)

                    fov_recompute = True # Recompute the FOV upon movement

                game_state = GameStates.ENEMY_TURN # Sets state to players turn.

        if exit:
                return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
# Iterate through the results
        # Player Results Loop
        for player_turn_result in player_turn_results: 
            message = player_turn_result.get('message') # Get the message part
            dead_entity = player_turn_result.get('dead') # Get the part as to whether dead or not

            if message:
                message_log.add_message(message) # Prints any messages for the player turn

            if dead_entity: # Check is something dead this turn
                if dead_entity == player: # Is the dead thing the player?
                    message, game_state = kill_player(dead_entity) # Run kill_player function
                else:
                    message = kill_monster(dead_entity) # Run kill_monster function

                message_log.add_message(message)
        # Enemy Results Loop
        if game_state == GameStates.ENEMY_TURN: # Checks to see if enemy turn
            for entity in entities: # Cycles through entities looking for monsters
                if entity.ai: # If entity is not the player and has ai.
                    # Set a list that calls the take_turn function for the ai
                    enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)

                    for enemy_turn_result in enemy_turn_results: # Iterate through the list
                        message = enemy_turn_result.get('message') # Gather any messages for that ai
                        dead_entity = enemy_turn_result.get('dead') # get and dead comments

                        if message:
                            message_log.add_message(message) # Print any messages for the turn of the ai

                        if dead_entity: # Check if dead entity this turn
                            if dead_entity == player: # Is it the player?
                                message, game_state = kill_player(dead_entity) # If yes then run kill_player and show message from results
                            else:
                                message = kill_monster(dead_entity) # If it's the monster, then kill it.

                            message_log.add_message(message)

                            if game_state == GameStates.PLAYER_DEAD: # Did the player die?
                                break # If dead player then end game.

                    if game_state == GameStates.PLAYER_DEAD:
                        break # Ends game if player dies and monster has died at same time.

            else:
            # Set the game_state back to players turn
                game_state = GameStates.PLAYERS_TURN

if __name__ == '__main__': # Declare the main function to be called
     main()