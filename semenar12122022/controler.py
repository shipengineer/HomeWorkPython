from tictokchecker import get_result
import tictok
from view import print_maps
import ticktok_init as ti


def new_game():
    game_run = True

    while game_run == True:
        print_maps()
        res = tictok.game()
        tictok.step_maps(*res)
        print(res)
        get_result()


new_game()
