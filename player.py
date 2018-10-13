import random
from entity import Entity
from room import Room

class Player(Entity) :
    num_enemy_types = 1;

    def __init__(self, name):
        self.name = name
        self.init_stats()
        Entity.__init__(self)

    def get_player_name(self) :
        return self.name

    def set_player_name(self, name):
        self.name = name

    def get_name(self) :
        toReturn = ""
        for adj in self.get_adjectives() :
            toReturn = toReturn + adj + " "
        return toReturn + self.get_player_name()

    def reset_all_stats() : #Reset all stats and health
        self.curr_stats = self.base_stats

    def partial_reset_stats() :
        for i in range(0, len(curr_stats)) :
            if(curr_stats[i] > base_stats[i] + 1) :
                delta = curr_stats[i] - base_stats[i]
                curr_stats[i] -= (delta / 2)
            elif(curr_stats[i] < base_stats[i] - 1) :
                delta = base_stats[i] - curr_stats[i]
                curr_stats += (delta / 2)
            else :
                curr_stats[i] = base_stats[i]
