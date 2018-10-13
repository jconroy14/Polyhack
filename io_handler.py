import entity
from player import Player

def combat_menu(player):

    print("You can use: " + str(", ".join(player.get_attacks())))

    while(True):
        option = input(">> ").lower() #user chooses which option
        valid_inputs = player.get_attacks()

        valid_inputs.append("list")
        if(option in valid_inputs):
            if (option == "list"):
                list_attacks(player) #takes array from andrew
            else:
                return option #takes array from andrew
        else:
            print("Input not valid")


def list_attacks(player):
    for a in player.get_attacks():   #if the value is in array
        print (a)

def input_attack(player):
    option = input('What attack do you want to use? ')
    if option in player.get_attacks():
        return option
    else:
        print ("Attack not learned.")
        return combat_menu(player)


def ui_intro():
    print("Welcome to *insert yet another mythical sounding world name*")
    print("You wake up in a strange room you don't recognize")
    print("The air is seriously thick, it tastes like golem smells")
    return

def ui_prompt_player_name():
    name = input("You haven't forgotten your name, right? Enter it here: ")
    return name
