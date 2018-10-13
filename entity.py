import random

class Entity :
    def __init__(self, name):
        self.adjectives = []; # string[]
        self.base_stats = []; # int[]
        self.curr_stats = []; # int[]

    # Returns string[] adjectives
    def get_adjectives(self) :
        return self.adjectives

    # Adds the one string argument to adjectives
    def give_adjective(self, adj) :
        self.adjectives.append(adj)

    # Returns int[] current stats
    def get_curr_stats(self) :
        return self.curr_stats

    # Sets current stats to input int[]
    def set_curr_stats(self, stats) :
        self.curr_stats = stats

    # Returns int[] base stats
    def get_base_stats(self):
        return self.base_stats

    #give rand adj
    def give_rand_adj(self) :
        self.give_adjective(random.choice(get_all_adjectives()))

    # Returns string[] attacks
    def get_attacks(self) :
        toReturn = []
        for adj in self.adjectives :
            toReturn.append()
