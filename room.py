from direction import direction, dir_input_mappings
import random
import enemy
import combat_handler

def getInput():
    return input("Waiting: ")

# fake methods for testing
def createMob(a_level):
    return "mob" #mobs are just an int

def mob_getDescription():
    return "A wild mob has appeared!"

def enterCombat(aMob,aPlayer):
    return True

def stairway_function(x):
    return 0.1*x;

class Room:
    #constructor
    def __init__(self, player, level, count, previous_room = None,\
                previous_direction = None):
        #member variables
        self.stairway = (random.uniform(0,1) < stairway_function(count))
        self.player = player
        self.level = level
        self.count = count
        self.available_passageways = []
        self.next_rooms = {1: None, -1: None, 2:None, -2:None, 3:None, -3:None,\
        4:None, -4:None, 9:None}
        self.combat = False

        if(previous_room is not None):
            self.available_passageways.append(previous_direction)
            self.next_rooms[previous_direction] = previous_room

        if(random.randint(0,1) > 0):
            self.combat = True;

        num_passages = random.randint(1,3)
        for i in range(num_passages):
            valid_new_passages = set([1,-1,2,-2,3,-3,4,-4]) - set(self.available_passageways)
            passage_to_add = random.sample(valid_new_passages,1)[0]
            self.available_passageways.append(passage_to_add)

    #main method for room
    def explore_room(self):
        print("\nThis is a room!")
        if(self.combat):
            mob = enemy.enemy(self.level);
            print(mob.get_name())
            if(not combat_handler.doCombat(mob,self.player)):
                return False;

        self.output_move_options()
        input = getInput()
        input_num = self.sanitize_input(input)
        return self.explore_next_room(input_num)

    def output_move_options(self):
        for curr_dir in self.available_passageways:
            print("There is a passage leading " + str(direction(curr_dir).name))

        if(self.stairway):
            print("There is a stairway going up...")

    #either get stuck in an endless loop or return a valid input (int)
    def sanitize_input(self,an_input,dir_value = None):
        an_input = an_input.lower()
        #validate input is direction
        valid_dir = False;
        for mapping in dir_input_mappings:
            if an_input in list(mapping.keys())[0]:
                valid_dir = True
                dir_value = list(mapping.values())[0].value
        if(not valid_dir):
            print("That is not a direction")
            an_input = getInput()
            return self.sanitize_input(an_input)

        #edge case: stair – this is sanitized
        if(dir_value==9 and self.stairway):
            return 9;

        #validate direction is not wall
        if(dir_value in self.available_passageways):
            return dir_value
        else:
            print("There is a wall that way!")
            an_input = getInput()
            return self.sanitize_input(an_input)

    def explore_next_room(self,direction_int):
        if(direction_int==9):
            print("DONE")
            return True

        print("exploring!")
        if(self.next_rooms[direction_int] is not None):
            self.next_rooms[direction_int].explore_room()
        else:
            room_to_add = Room(self.player,self.level,self.count+1,self,-1 * direction_int)
            self.next_rooms[direction_int] = room_to_add
            return room_to_add.explore_room()
