import libtcodpy as libtcod
from game_states import GameStates
from render_functions import RenderOrder
from game_messages import Message

# Call this function if player is killed
def kill_player(player):
    player.char = '%' # Change character
    player.color = libtcod.dark_red # Make the character red

    # return 'You died!', GameStates.PLAYER_DEAD  -- Replaced print with Message Class
    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD
    # Send message you died to the dead function in game_states

# Call this function if monster is killed on a turn
def kill_monster(monster):
    # death_message = '{0} is dead!'.format(monster.name.capitalize()) -- replaced with Message Class
    # Show that monster is dead
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)
    monster.char = '%' # Change monster's character
    monster.color = libtcod.dark_red # Change color of charactter
    monster.blocks = False # You can now walk over a dead monster
    monster.fighter = None # This monster will no longer fight you
    monster.ai = None # And the monster can no longer move
    monster.name = 'remains of ' + monster.name # Change the name of the monster.
    monster.render_order = RenderOrder.CORPSE # Changes monster to render of corpse.

    return death_message # Send death message to calling function.