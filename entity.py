class Entity :
	def __init__(self, name):
        self.adjectives = []; # string[]
		self.base_stats = []; # int[]
		self.curr_stats = []; # int[]
	
	# Returns string[] adjectives
	def get_adjectives(self) :
		return self.adjectives
		
	# Adds the one string argument to adjectives
	def add_adjective(self, string adj) :
		self.adjectives.append(adj)
		
	# Returns int[] current stats
	def get_curr_stats(self) :
		return self.curr_stats
		
	# Sets current stats to input int[]
	def set_curr_stats(self, int[] stats) :
		self.curr_stats = stats
		
	# Returns int[] base stats
	def get_base_stats(self)
		return self.base_stats
		
	# Returns string[] attacks
	def get_attacks(self) :
		toReturn = []
		for adj in self.adjectives :
			toReturn.append()