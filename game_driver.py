import io_handler as ui
from player import Player
from room import Room

def run_game() :
    ui.ui_intro()
    name = ui.ui_prompt_player_name()
    player = Player(name)
    alive = True
    level = 1
    while(alive) :
        player.give_rand_adj()
        firstRoom = Room(player, level, 0)
        alive = firstRoom.explore_room()
        print("alive: " + str(alive))
        level += 1
        print(chr(27) + "[2J")
        print("LEVEL " + str(level))


def main() :
    run_game();

if __name__ == '__main__':
    main()
