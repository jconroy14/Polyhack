import entity
import player

def combat_menu(player):

    print("1. list attacks")
    print("2. Enter attack")

    option = int(input) #user chooses which option, TODO: sanitize

    while(True):
        if (option == 1):
            list_attacks(player) #takes array from andrew
        elif (option == 2):
            return input_attack(player) #takes array from andrew
        else:
            print("You don't know that move, please try again!") #retry entry
    return


def list_attacks(player):
    for a in player.get_attacks():   #if the value is in array
        print (a)
    return


def input_attack(player):
    while (True):
        option = input('What attack do you want to use? ')
        if option in player.get_attacks():
            return option
        else:
            print ("Attack not learned. What attack do you want to use?")
    return


def ui_intro():
    print("Welcome to *insert yet another mythical sounding world name*")
    print("You wake up in a strange room you don't recognize")
    print("The air is seriously thick, it tastes like golem smells")

    return

def ui_prompt_player_name():
    name = input("You haven't forgotten your name, right? Enter it here: ")

    return name
