# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достатся сделавшему последний ход.
# a) Добавьте игру против бота

from tkinter import *
import random
# Первичная инициация
root = Tk()
vase = 117
order = random.choice([True, False])
player1 = 0
player2 = 0
hand = 0

# функция смены выделения игрока


def buttonActivation():
    if order:
        player1Grab['state'] = "normal"
        player1Grab['background'] = '#0CDF1B'
        player1Hand['state'] = 'normal'

        player2Grab['state'] = "disabled"
        player2Grab['background'] = '#CA5149'
        player2Hand['state'] = 'disable'

    else:
        player1Grab['state'] = "disabled"
        player1Grab['background'] = '#CA5149'
        player1Hand['state'] = 'disable'
        player1Hand['text'] = ''

        player2Grab['state'] = "normal"
        player2Grab['background'] = '#0CDF1B'
        player2Hand['state'] = 'normal'
        player2Hand['text'] = ''
    player1Hand.delete(0, END)
    player2Hand.delete(0, END)

# функция новой игры


def newGame():
    vase = 117
    order = random.choice([True, False])
    buttonActivation()
    vaseButton['text'] = vase
    player1Button['text'] = f"Игрок 1\n{player1}"
    player2Button['text'] = f"Игрок 2\n{player2}"
    winner['height'] = 6
    winner['text'] = f'Тянет игрок №{ 1 if  order  else 2}'
    winner['font'] = ('Arial', 12)
    winner['background'] = '#FFFFFF'

# функция хода


def round():
    global vase, order, player1, player2
    if vase > 0:
        if order:  # Если ходит первый игрок
            hand = int(player1Hand.get())
            print(hand)
            if hand > 28:
                hand = 28
            if hand < 0:
                hand = 0
            vase -= hand
            player1 += hand
            player1Button['text'] = f"Игрок 1\n{player1}"
            winner['text'] = f'Тянет игрок №{ 1 if  order  else 2}'
        else:  # Если ходит второй игрок
            hand = int(player2Hand.get())
            print(hand)
            if hand > 28:
                hand = 28
            if hand < 0:
                hand = 0
            vase -= hand
            player2 += hand
            player2Button['text'] = f"Игрок 2\n{player2}"
        order = not order
        vaseButton['text'] = vase
        winner['text'] = f'Тянет игрок №{1 if  order  else 2}'
        if vase <= 0:  # Конец игры
            vaseButton['text'] = '0'
            vase = 117
            winner['height'] = 10
            winner['background'] = '#8C49CA'
            winner['text'] = f'Выйграл игрок №{1 if  order == True else 2}'
            winner['font'] = ('Arial', 20, 'bold')
            player1 = 0
            player2 = 0
            hand = 0
    buttonActivation()


# Создание и верстка элементов
vaseButton = Button(root, width=5, height=1,
                    text=f'{vase}',
                    font='Arial 24 bold')
vaseButton.grid(row=3, column=1)

player1Button = Button(root, width=10, height=2, text=f"Игрок 1\n{player1}")
player1Button.grid(row=0, column=0)

player2Button = Button(root, width=10, height=2, text=f"Игрок 2\n{player2}")
player2Button.grid(row=0, column=3)

player1Hand = Entry(root, borderwidth=3, width=10)
player1Hand.grid(row=1, column=0)

player2Hand = Entry(root, borderwidth=3, width=10)
player2Hand.grid(row=1, column=3)

player1Grab = Button(root, width=15, height=2,
                     text="Взять конфеты", command=round)
player1Grab.grid(row=2, column=0)

player2Grab = Button(root, width=15, height=2,
                     text="Взять конфеты", command=round)
player2Grab.grid(row=2, column=3)

winner = Button(root, height=6, width=16,
                text=f'Тянет игрок №{1 if  order == True else 2}',
                font="Arial 12", background='#FFFFFF')
winner.grid(row=0, column=1)

newGameButton = Button(root, height=2, width=10,
                       command=newGame, text='Новая игра')
newGameButton.grid(row=4, column=0)

buttonActivation()
root.mainloop()
