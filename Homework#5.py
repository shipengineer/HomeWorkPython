from tkinter import *
import random
root = Tk()
root.title('Tik-Tok')
gameRun = True
field = []
crossCount = 0
scndPlayer = False
circleCount = 0
order = True


def ask(arg):
    if arg:
        global scndPlayer
        scndPlayer = True
        askSecondPlayer['background'] = 'yellow'
        askBOT['background'] = '#A8E4A0'
        newGame()
    else:
        scndPlayer = False
        askSecondPlayer['background'] = '#A8E4A0'
        askBOT['background'] = 'yellow'
        newGame()
# Инициализация новой игры


def newGame():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global gameRun, crossCount, order
    gameRun = True
    crossCount = 0
    order = True


# Фунция установки крестика


def click(row, col):
    if gameRun and field[row][col]['text'] == ' ':
        global order
        if order == True:
            field[row][col]['text'] = 'X'
            global crossCount
            crossCount += 1
            checkWin('X')
            if gameRun and crossCount < 5 and scndPlayer == False:
                computerMove()
                checkWin('O')
            else:
                order = False
        else:
            field[row][col]['text'] = 'O'
            global circleCount
            circleCount += 1
            checkWin('O')
            order = True


# Проверка на победу


def checkWin(smb):
    for n in range(3):
        checkLine(field[n][0], field[n][1], field[n][2], smb)
        checkLine(field[0][n], field[1][n], field[2][n], smb)
    checkLine(field[0][0], field[1][1], field[2][2], smb)
    checkLine(field[2][0], field[1][1], field[0][2], smb)

# Отображение победы


def checkLine(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'yellow'
        global gameRun
        gameRun = False

# Функция поиска удачного хода


def winPossible(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

# Перебор полей или случайный ход


def computerMove():
    for n in range(3):
        if winPossible(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if winPossible(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if winPossible(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if winPossible(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if winPossible(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if winPossible(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if winPossible(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if winPossible(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=newGame)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

askBOT = Button(root, text='Против БОТА', width=5, height=1,
                font=('Trebuchet', 10, 'bold'),
                background="#A8E4A0",
                command=lambda arg=False: ask(arg))
askBOT.grid(row=4, column=0, columnspan=3, sticky='nsew')


askSecondPlayer = Button(root, text='Против ИГОКА', width=5, height=1,
                         font=('Trebuchet', 10, 'bold'),
                         background="#A8E4A0",
                         command=lambda arg=True: ask(arg))
askSecondPlayer.grid(row=5, column=0, columnspan=3, sticky='nsew')


root.mainloop()
