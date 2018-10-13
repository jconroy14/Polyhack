import random
from entity import Entity
import content_handler

class enemy(Entity) :
    #Health, Attack, Defense, Evasion
    num_enemy_types = 2;

    def __init__(self, level) :
        Entity.__init__(self)
        self.level = level
        self.enemy_type = random.randint(0,self.num_enemy_types)
        self.init_stats()
        for i in range(0, level) :
            self.give_rand_adj()

    def get_random_attack_name(self) :
        return random.choice(self.get_attacks())

    def get_enemy_type(self) :
        return content_handler.get_enemy_type(self.level,self.enemy_type) #TODO

    def get_name(self) :
        toReturn = ""
        for adj in self.get_adjectives() :
            toReturn = toReturn + adj + " "
        return toReturn + self.get_enemy_type()

    def init_stats(self) :
        self.base_stats = [5, 5, 5, 20]
        self.curr_stats = self.base_stats
