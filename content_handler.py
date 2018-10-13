
def create_dict ():
    with open("adjective_book.csv", "r") as file:
        adjective_book_dict = {}
        for line in file:
            line = line.split()
            key = line [0]
            values = []
            for word in line:
                if word != key:
                    values.append(int(word))
            adjective_book_dict[key] = values
    return adjective_book_dict

def create_str_dict(variable_file):
    with open(variable_file, "r") as file:
        str_dict = {}
        for line in file:
            line = line.split(',')
            key = line [0]
            values = line [1]
            str_dict[key] = values
    return str_dict

def get_all_adjectives() :
    toReturn = []
    for adj in get_adj_book_dict1_dict() :
        toReturn.append(adj)

def get_theme_enemy_dict():
    return create_str_dict()
def get_flr_theme_descrip_dict():
    return create_str_dict("flr_theme_descrip.csv")
def get_adj_atk_descrip_dict():
    return create_str_dict("adj_attack.csv")
def get_adj_book_dict1_dict():
    return create_dict()
