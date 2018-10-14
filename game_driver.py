import io_handler as ui
from player import Player
from room import Room
import os
import content_handler

def run_game() :
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.ui_intro()
    name = ui.ui_prompt_player_name()
    player = Player(name)
    alive = True
    level = 0
    while(alive) :
        player.give_rand_adj()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("LEVEL " + str(level))
        print("You are " + ", ".join(player.get_adjectives()))
        print("You have " + str(player.get_curr_stats()[0]) + " health\n")
        print("You see " + content_handler.get_theme(level) + ": " + \
            str(content_handler.get_flr_theme_descrip_dict()[content_handler.get_theme(level)]))

        firstRoom = Room(player, level, 0)
        alive = firstRoom.explore_room()
        level += 1
        if level >= 10 :
            break

    again = input("Play again? (y/n)")
    if(again == "y"):
        run_game()
    else:
        print("Thanks for playing!")

def main() :
    run_game()

if __name__ == '__main__':
    main()
