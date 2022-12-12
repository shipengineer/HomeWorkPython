import tictok as ti

def get_result():
    win = ""

    for i in ti.victories:
        if ti.maps[i[0]] == 'X' and ti.maps[i[1]] == 'X' and ti.maps[i[2]] == 'X':
            win = 'X'
            game_over =True
        if ti.maps[i[0]] == 'O' and ti.maps[i[1]] == 'O' and ti.maps[i[2]] == 'O':
            win = 'O'
            game_over =True

    return win