import random
import io_handler

HEALTH_INDEX = 0
ATK_INDEX = 1
DEF_INDEX = 2
EVAS_INDEX = 3


def do_attack(attack_name, one, two) : # one attacks two
    effect = get_attack_effect(attack_name)
    if (evas_success(two) == True):
        output("Miss!")
    else:
        calculate_effects(effect, one, two)
        output(get_attack_description(attack_name))


def calculate_effects(effect, one, two) :
        #add each value in array effect into corresponding index
        #of array contained by entity

        one_curr_stats = one.get_curr_stats()
        two_curr_stats = two.get_curr_stats()

        if (one_curr_stats[ATK_INDEX] > two_curr_stats[DEF_INDEX]):
            damage = one_curr_stats[ATK_INDEX] - two_curr_stats[DEF_INDEX]
            two_curr_stats[HEALTH_INDEX] -= damage


        for i in effect:
            if (two_curr_stats[i] + effect[i] < 0) :
                two_curr_stats[i] = 0
            else :
                two_curr_stats[i] += effect[i]



def evas_success(two):
    rand_num = random() * 100
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
    print("player stats: " + str(player.get_curr_stats()))
    player_health = player.get_curr_stats()[HEALTH_INDEX]
    enemy_health = enemy.get_curr_stats()[HEALTH_INDEX]

    attack_choice = io_handler.combat_menu(player)

    while (player_health > 0 and enemy_health > 0) :
        do_attack(attack_choice, player, enemy)
        do_attack(enemy.get_rand_attack_name(), enemy, player)


    if (player_health <= 0) :
        return False
    else :
        player.partial_reset_stats()
        return True



####################################
