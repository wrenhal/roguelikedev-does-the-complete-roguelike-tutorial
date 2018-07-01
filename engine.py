# This will be my working main file for the RogueLike tutorial
# Renaming to engine.py to follow http://rogueliketutorials.com/libtcod/1

import libtcodpy as libtcod # Imports the Graphics library
# Now adding import of the handle_keys() function
from input_handlers import handle_keys

def main(): # Adding the main function for Python 3 compatibility

# Setting constants
    screen_width = 80
    screen_height = 50
    # LIMIT_FPS = 20 # Unused for now
    # Setting player coordinate starting point at center of console
    player_x = int(screen_width / 2) 
    player_y = int(screen_height / 2)
# Initializing the library font
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# Now creating the window with size constants, title, and whether fullscreen
    libtcod.console_init_root(screen_width, screen_height, 'python/libtcod tutorial', False)
    # libtcod.sys_set_fps(LIMIT_FPS) # Good for Realtime, if turn based can comment out

    key = libtcod.Key()  # Setting keyboard variable for input
    mouse = libtcod.Mouse() # Setting mouse variable for input
    
# Next is the main game loop.  We basically print the @ character to the screen in white
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        libtcod.console_set_default_foreground(0, libtcod.white) # 0 represents the created window
        # libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE) # 1,1 represents the coordinates
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush() # Flush the console which writes any changes to the screen
  
        # key = libtcod.console_check_for_keypress() # Initializing Libtcod Keyboard support
        # if key.vk == libtcod.KEY_ESCAPE: # Checking for ESC key to close window
# New setup to call handle_keys() function from input_handlers.py
        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if exit:
                return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen)

if __name__ == '__main__': # Declare the main function to be called
     main()