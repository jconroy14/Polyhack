import io_handler as ui
from player import Player

def run_game() :
    print("hi")
    ui.ui_intro()
    name = ui.ui_prompt_player_name()
    player = Player(name)
    alive = True
    level = 1
    while(alive) :
        player.give_rand_adj()
        firstRoom = Room(player, level)
        alive = firstRoom.explore_room()
        level += 1


def main() :
    run_game();

if __name__ == '__main__':
    main()
