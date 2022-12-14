# Exercise #2.1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import random


def sumElem(elem):
    result = 0
    massElem = str(elem)
    for i in range(len(massElem)):
        if massElem[i] != ",":
            result += int(massElem[i])
        else:
            continue
    print(result)


# vvodnoe = input("Чсило для первой задачи = ")
# sumElem(vvodnoe)

# ____________________________________________________________________________________________________


# Exercise #2.2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def fill(a):
    if a == 1:
        return 1
    else:
        return a * fill(a-1)


def nabor(elem):
    result = []
    for i in range(1, elem):
        result.append(fill(i))
    print(result)

# vvodnoe2 = input("Число для второй задачи: ")
# nabor(vvodnoe2)
# ____________________________________________________________________________________________________

# Exercise #2.3
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]


def e23(n):
    result23 = []
    sum = 0
    for i in range(0, n):
        result23.append((1+1/(i+1))**(i+1))
        sum += result23[i-1]
    print(result23)
    print(f"Сумма последовательности равна: {sum}")


# vvodnoe23 = int(input("Введите число для третьей задачи: "))
# e23(vvodnoe23)
# ____________________________________________________________________________________________________


# Exercise #2.4

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
# with open("file.txt", "r") as f:
#     firstIndex = int(f.readline())
#     secondIndex = int(f.readline())


def collection(n):
    result24 = []
    for i in range(-n, n+1):
        result24.append(i)
    print(result24)
    mult = result24[firstIndex]*result24[secondIndex]
    print(mult)


# vvodnoe24 = int(input("Введите число для четвертой задачи: "))
# print(f"Вы выбрали {firstIndex} и {secondIndex} места в массиве для умножения")
# collection(vvodnoe24)
# ____________________________________________________________________________________________________


# Exercise #2.5
# Реализуйте алгоритм перемешивания списка.


def ignore(vodMas, count):
    n = 0
    while n in vodMas:
        n = random.randint(0, count*2-1)

    vodMas.append(n)
    return n


def shuffleMas(mas):
    ignoreMas = []
    count = int(len(mas)/2)
    # print(count)
    for i in range(count):
        first = ignore(ignoreMas, count)
        second = ignore(ignoreMas, count)
        swap = mas[first]
        mas[first] = mas[second]
        mas[second] = swap
    print(f"Перемешанный массив: {mas}")


a = ["1", "2", "3", "4", "5", "6"]

shuffleMas(a)
# ____________________________________________________________________________________________________
