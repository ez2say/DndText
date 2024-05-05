import input_data
from Dungeon import fork
from Dungeon.Dungeon_top import forest
from Dungeon.Dungeon_top import enemy_top
from Dungeon.Dungeon_top import swamp
from Dungeon.Dungeon_top import location



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
    char = fork.create_char()
    new_hero = fork.set_name(char)
    complete_hero = fork.hero_choise(new_hero)
    print(complete_hero)
    if complete_hero :
        chs = fork.first_fork()
        if chs == 1:
            enemy_dict = enemy_top.enemy_list
            dict_forest = location.forest_dict
            forest.forest_info(dict_forest)
            forest.fight_text(dict_forest)
            forest.first_fight(complete_hero,enemy_dict)
        elif chs == 2:
            pass
        else:
            pass





























    #dict_forest = location.forest_dict
    #hero = fork.hero_choise()
    #enemy = enemy_top.enemy_list
    #choise = fork.first_fork()
    #if choise == 1:
        #forest.forest_info(dict_forest)
        #forest.first_fight(dict_forest,hero, enemy)
        #go_to = forest.second_fork()
        #if go_to == 1:
           # forest.zemlyanka(dict_forest,hero)
            #forest.after_zemlyanka()
            #way = forest.deep_forest()
           # if way == 1:
           #     swamp.swamp()
          #  else:
            #    forest.third_fork()
       # else:
         #   forest.deep_forest()
#









