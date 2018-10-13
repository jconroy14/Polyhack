import entity
from player import Player

def combat_menu(player):

    print("1. list attacks")
    print("2. Enter attack")

    while(True):
        option = input("Your choice: ") #user chooses which option
        try:
            option = int(option)
        except:
            print("Please input the number of your choice")
        if (option == 1):
            list_attacks(player) #takes array from andrew
        elif (option == 2):
            return input_attack(player) #takes array from andrew
        else:
            print("Number not valid") #retry entry


def list_attacks(player):
    for a in player.get_attacks():   #if the value is in array
        print (a)


def input_attack(player):
    while (True):
        option = input('What attack do you want to use? ')
        if option in player.get_attacks():
            return option
        else:
            print ("Attack not learned. What attack do you want to use?")


def ui_intro():
    print("Welcome to *insert yet another mythical sounding world name*")
    print("You wake up in a strange room you don't recognize")
    print("The air is seriously thick, it tastes like golem smells")
    return

def ui_prompt_player_name():
    name = input("You haven't forgotten your name, right? Enter it here: ")
    return name
