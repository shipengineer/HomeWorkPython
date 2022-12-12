# карта позиций
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
# Выигрышные позиции
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def game():
    game_over = False
    player1 = True
    while game_over == False:
        if player1 == True:
            symbol = 'X'
            step = int(input('Игрок 1, Ваш ход!'))
        else:
            symbol = 'O'
            step = int(input('Игрок 2, Ваш ход!'))
        player1 = not (player1)
    
        return step, symbol
