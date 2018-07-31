# Game state file to keep track of things such as player or monster turns

from enum import Enum


class GameStates(Enum):
    PLAYERS_TURN = 1
    ENEMY_TURN = 2


