def get_theme(num) :
    if num == 0 :
        return "Hilly University"
    elif num == 1:
        return "The Mall"
    elif num == 2:
        return "Winter Wonderland"
    elif num == 3:
        return "Volcano"
    elif num == 4:
        return "Sky"
    elif num == 5:
        return "The Flintstone's Cave"
    elif num == 6:
        return "Under the Sea"
    elif num == 7:
        return "Forest"
    elif num == 8:
        return "Desert"
    elif num == 9:
        return "Haunted House"



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
            values = line [1]
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
def get_flr_theme_descrip_dict(): #str to str theme to description
    return create_str_dict("Content/flr_1_descrip.csv")
def get_adj_atk_descrip_dict():
    return create_str_dict("Content/adj_attack.csv")
def get_adj_book_dict1_dict():
    return create_dict()
