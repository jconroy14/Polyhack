
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

