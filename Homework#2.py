# Exercise #2.1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

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

# vvodnoe2 = input("Число для второй задачи")
# nabor(vvodnoe2)
# ____________________________________________________________________________________________________

# Exercise #2.3
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]


def e23(n):
    result23 = []
    sum = 0
    for i in range(n):
        result23[i] = (1+1/n)**n
        sum = + result23[i]
    print(result23)
    print(sum)


vvodnoe23 = input("Введите чсло для третьей задачи")
e23(vvodnoe23)
