import random
from entity import Entity
from room import Room

class Player(Entity) :
    num_enemy_types = 1;

    def __init__(self, name):
        Entity.__init__(self)
        self.name = name
        self.init_stats()

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

    def partial_reset_stats(self) :
        for i in range(0, len(self.curr_stats)) :
            if(self.curr_stats[i] > self.base_stats[i] + 1) :
                delta = self.curr_stats[i] - self.base_stats[i]
                self.curr_stats[i] -= (delta / 2)
            elif(self.curr_stats[i] < self.base_stats[i] - 1) :
                delta = self.base_stats[i] - self.curr_stats[i]
                self.curr_stats += (delta / 2)
            else :
                self.curr_stats[i] = self.base_stats[i]
