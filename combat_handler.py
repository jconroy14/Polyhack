import random
import io_handler
import content_handler

HEALTH_INDEX = 0
ATK_INDEX = 1
DEF_INDEX = 2
EVAS_INDEX = 3


def do_attack(attack_name, one, two) : # one attacks two
    effect = content_handler.get_attack_effect(attack_name)
    if (evas_success(two) == True):
        if(one.__class__.__name__ == "Player"):
            print("You miss!")
        else:
            print("Enemy misses!")
    else:
        calculate_effects(effect, one, two)
        if(one.__class__.__name__ == "Player"):
            print("You " + str(content_handler.get_attack_description(attack_name)) + " attack the " + str(two.get_name()) + "!")
        else:
            print("The " + one.get_name() + " " + str(content_handler.get_attack_description(attack_name)) + " attack you!")



def calculate_effects(effect, one, two) :
        #add each value in array effect into corresponding index
        #of array contained by entity

        one_curr_stats = one.get_curr_stats()
        two_curr_stats = two.get_curr_stats()

        if (one_curr_stats[ATK_INDEX] > two_curr_stats[DEF_INDEX]):
            damage = one_curr_stats[ATK_INDEX] - two_curr_stats[DEF_INDEX]
            two_curr_stats[HEALTH_INDEX] -= damage


        for i in range(0,len(effect)):
            if (two_curr_stats[i] + effect[i] < 0) :
                two_curr_stats[i] = 0
            else :
                two_curr_stats[i] += effect[i]


def evas_success(two):
    rand_num = random.uniform(0,100)
    evas_chance = two.get_curr_stats()[EVAS_INDEX]

    if (rand_num < evas_chance) :
        return True
    else :
        return False


####################################
#
#
#Combat Phase
####################################

def do_combat(player, enemy):
    player_health = player.get_curr_stats()[HEALTH_INDEX]
    enemy_health = enemy.get_curr_stats()[HEALTH_INDEX]

    while (player_health > 0 and enemy_health > 0) :
        attack_choice = io_handler.combat_menu(player)
        do_attack(attack_choice, player, enemy)
        do_attack(enemy.get_random_attack_name(), enemy, player)

        # print("STATUS: ")
        # print("Player: " + str(player.get_curr_stats()))
        # print("Enemy: " + str(enemy.get_curr_stats()))

        player_health = player.get_curr_stats()[HEALTH_INDEX]
        enemy_health = enemy.get_curr_stats()[HEALTH_INDEX]

    if (player_health <= 0) :
        print("You have been eaten by a grue")
        return False
    else :
        print("You defeated the " + enemy.get_name() + "!")
        print("You have " + str(player.get_curr_stats()[0]) + " health left\n")
        player.partial_reset_stats()
        return True



####################################
