# Base Monster class 
import libtcodpy as libtcod

class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y): # Checks to see if monster is in FOV of player

            if monster.distance_to(target) >= 2: # Check to see if monster is greater than or equal to 2 moves from player
                monster.move_astar(target, entities, game_map) # If so then move toward the player

            elif target.fighter.hp > 0: # If in FOV and closer than 2 steps (1 ha ha) then attack the player
                attack_results = monster.fighter.attack(target) # Monster attacks player
                results.extend(attack_results) # results of the attack are added into the list

        return results # return results to the calling function