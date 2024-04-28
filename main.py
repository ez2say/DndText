import input_data
from Dungeon import fork
from Dungeon.Dungeon_top import forest
from Dungeon.Dungeon_top import enemy_top



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
    hero = fork.hero_choise()
    enemy = enemy_top.enemy_list
    fork.history()
    choise = fork.first_fork()
    if choise == 1:
        forest.forest_info()
        forest.first_fight(hero, enemy)
        go_to = forest.second_fork()
        if go_to == 1:
            forest.zemlyanka(hero)
            forest.after_zemlyanka()
            forest.deep_forest()
        else:
            forest.deep_forest()










