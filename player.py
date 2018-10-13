import random

class Player(Entity) :
	num_enemy_types = 1;
	
	def __init__(self, name):
        self.name = name
		
	def give_rand_adj(self) :
		self.give_adjective(choice(get_all_adjectives()))
		
	def get_player_name(self) :
		return self.name
	
	def set_player_name(self, name) :
		self.name = name
	
	def get_name(self):
		toReturn = ""
		for adj in self.get_adjectives() :
			toReturn = toReturn + adj + " "
		return toReturn + self.get_player_name()