import random
import entity
import flavor_handler

class Enemy(Entity) :
	#Health, Attack, Defense, Evasion
	num_enemy_types = 1;
	
	def __init__(self, level) :
        enemy_type = random() * num_enemy_types;
		
	def get_random_attack_name(self) :
		return choice(self.get_attacks())
		
	def get_enemy_type(self) :
		return flavor_handler.get_enemy_type(enemy_type) #TODO
		
	def get_name(self) :
		toReturn = ""
		for adj in self.get_adjectives() :
			toReturn = toReturn + adj + " "
		return toReturn + self.get_enemy_type()
	
	def init_stats(self) :
		base_stats = {100, 10, 10, 10}
		curr_stats = base_stats