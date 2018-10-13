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
##def main ():
  ##  print 'start'
    ##adjective_book_dict1 = {}
   ## adjective_book_dict1 = create_dict()
   ## adj_atk_descrip = create_str_dict("adj_attack.csv")
   ## print adj_atk_descrip
   ## for x in adj_atk_descrip:
     ##   print(x + " " + str(adj_atk_descrip[x]))
   ## print 'stop'

##if __name__ == '__main__' :
    main()
