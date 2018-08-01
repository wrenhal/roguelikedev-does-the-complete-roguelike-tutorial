# game_states.py
# separates out the logic ffor keeping track of turns in an enum 

from enum import Enum


class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2