import random

def get_theme(num) :
    if num == 0 :
        return "hilly university"
    elif num == 1:
        return "a mall"
    elif num == 2:
        return "a winter wonderland"
    elif num == 3:
        return "a volcano"
    elif num == 4:
        return "the sky"
    elif num == 5:
        return "the Flintstone's Cave"
    elif num == 6:
        return "under the Sea"
    elif num == 7:
        return "forest"
    elif num == 8:
        return "the desert"
    elif num == 9:
        return "a haunted house"



def create_dict ():
    with open("Content/adjective_book.csv", "r") as file:
        adjective_book_dict = {}
        for line in file:
            if line == "\n":
                continue
            line = line.split()
            key = line[0]
            values = []
            for word in line:
                if word != key:
                    values.append(int(word))
            adjective_book_dict[key] = values
    return adjective_book_dict

def create_str_dict(variable_file = "Content/theme_enemy.csv"):
    with open(variable_file, "r") as file:
        str_dict = {}
        for line in file:
            if line == "\n":
                continue
            line = line.split(',')
            key = line [0]
            values = []
            for word in line:
                if word != key:
                    values.append(word.rstrip())
            if(len(values)==1):
                str_dict[key] = values[0]
            else:
                str_dict[key] = values
    return str_dict

def get_all_adjectives() :
    toReturn = []
    for adj in get_adj_book_dict1_dict() :
        toReturn.append(adj)
    return toReturn

def get_enemy_type(level, type):
    theme = get_theme(level)
    return get_theme_enemy_dict()[theme][type]

def get_theme_enemy_dict(): #str to str[] theme to enemies
    return create_str_dict()
def get_flr_theme_descrip_dict(): #str to str, theme to description
    return create_str_dict("Content/flr_theme_descrip.csv")
def get_adj_atk_descrip_dict():
    return create_str_dict("Content/adj_attack.csv")
def get_adj_book_dict1_dict():
    return create_dict()
def get_adj_to_attack_dict():
    return create_str_dict("Content/adj_to_attack.csv")

def get_attack_effect(name_of_attack):
    if(name_of_attack == "slap"):
        return [0,0,0,0]
    #get adj from attack
    adj_to_attack = get_adj_to_attack_dict();
    attack = list(adj_to_attack.keys())[list(adj_to_attack.values()).index(name_of_attack)]

    return get_adj_book_dict1_dict()[attack]

def get_attack_description(name_of_attack):
    return get_adj_atk_descrip_dict()[name_of_attack]
