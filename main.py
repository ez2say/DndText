import input_data
from Dungeon import fork
from Dungeon.Dungeon_top import forest
from Dungeon.Dungeon_top import enemy_top
from Dungeon.Dungeon_top import swamp



def run():
    input_data.hello()
    input_data.menu()
    choize = input_data.choice()
    while True:
        if choize == '4':
            break
        try:
            if choize == 1:
                new_game()
                break
            elif choize == 2:
                pass
            elif choize == 3:
                pass
            else:
                input_data.alert()
                continue
        except Exception as ex:
            print(ex)


def new_game():
    dict_forest = forest.forest_dict
    hero = fork.hero_choise()
    enemy = enemy_top.enemy_list
    fork.history()
    choise = fork.first_fork()
    if choise == 1:
        forest.forest_info(dict_forest)
        forest.first_fight(dict_forest,hero, enemy)
        go_to = forest.second_fork()
        if go_to == 1:
            forest.zemlyanka(dict_forest,hero)
            forest.after_zemlyanka()
            way = forest.deep_forest()
            if way == 1:
                swamp.swamp()
            else:
                forest.third_fork()
        else:
            forest.deep_forest()










