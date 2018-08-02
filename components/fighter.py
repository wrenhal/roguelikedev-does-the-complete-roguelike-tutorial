# Base Fighter class that will include the Player and Monsters

class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount): # Function to compute damage
        results = [] # Create a Dictionary to store the results of the function
        self.hp -= amount 
        if self.hp <= 0: # Check to see if entity should be declared dead
            results.append({'dead': self.owner}) # If dead then send to results []

        return results # Send the list to calling function

    def attack(self, target): # Function to control attack and the call damage function
        results = [] # Create a dictionary to store the results of the function 
        damage = self.power - target.fighter.defense # Is power greater than defense?

        if damage > 0: # If so then calculate damage.
            # Place results into results [] (This includes a message showing damage done)
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage))})
            results.extend(target.fighter.take_damage(damage)) # This adds results from take_damage function.  Death message or nothing
        else: # If not greater then no damage
            # Place following message into results if no damage done
            results.append({'message': '{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name)})

        return results  # Return the list to the calling function.