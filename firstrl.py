import libtcodpy as libtcod # Imports the Graphics library
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
    libtcod.console_flush() # Flush the console which presents any changes to the screen
    