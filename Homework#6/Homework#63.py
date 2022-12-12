# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import math
spisok1 = [1, 2, 3, 4, 5, 6, 7, 1, 10]
proverka = [2, 3, 5, 9, 3]


def sumEven(mas):
    sum = 0
    for i in range(1, len(mas), 2):
        sum += mas[i]
    print(sum)

# ____________________________________________________________________________________________________

# модернизация


spisok1 = [1, 2, 3, 4, 5, 6, 7, 1, 10]
proverka = [2, 3, 5, 9, 3]
sum = 0
(lambda y: sum=sum + y) for x in (list(filter(lambda x: True if spisok1.index(x) %
                                              2 == 0 else False, spisok1)))
# sum = + x for x in spisok1 if spisok1.index(x) % 2 == 0
print(sum)
