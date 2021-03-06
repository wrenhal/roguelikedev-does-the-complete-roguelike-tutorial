# This was first attempt for the screen roguelike tutorial firstrl.py
# This allowed me to test my libtcod was setup properly
# Following this tutorial: http://rogueliketutorials.com/libtcod/1

import libtcodpy as libtcod # Imports the Graphics library


def main(): # Adding the main function for Python 3 compatibility

# Setting constants
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    LIMIT_FPS = 20
# Initializing the library font
    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
# Now creating the window with size constants, title, and whether fullscreen
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
    libtcod.sys_set_fps(LIMIT_FPS) # Good for Realtime, if turn based can comment out
# Next is the main game loop.  We basically print the @ character to the screen in white
    while not libtcod.console_is_window_closed():  
        libtcod.console_set_default_foreground(0, libtcod.white) # 0 represents the created window
        libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE) # 1,1 represents the coordinates
        libtcod.console_flush() # Flush the console which writes any changes to the screen

# Initial tutorial doesn't do the next lines at first.
# Without it the process becomes unresponsive on windows so I went straight to adding them.
  
        key = libtcod.console_check_for_keypress() #initializing Libtcod Keyboard support

        if key.vk == libtcod.KEY_ESCAPE: # Checking for ESC key to close window
                return True 

if __name__ == '__main__': # Declare the main function to be called
     main()