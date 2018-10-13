import io_handler as ui
from player import Player
from room import Room
import os

def run_game() :
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.ui_intro()
    name = ui.ui_prompt_player_name()
    player = Player(name)
    alive = True
    level = 1
    while(alive) :
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LEVEL " + str(level))
        print("You have " + str(player.get_curr_stats()[0]) + " health")

        player.give_rand_adj()
        firstRoom = Room(player, level, 0)
        alive = firstRoom.explore_room()
        level += 1

    again = input("Play again? (y/n)")
    if(again == "y"):
        run_game()

def main() :
    run_game();

if __name__ == '__main__':
    main()
