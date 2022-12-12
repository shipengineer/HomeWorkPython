# Exercise #2.5
# Реализуйте алгоритм перемешивания списка.
import random


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


# модификация
a = ["a", "b", "c", "d", "f", "g"]


def rndChoice(mas):
    mutable = mas
    result = []
    while mutable != []:
        x = random.choice(mutable)
        result.append(x)
        mutable.remove(x)
    return result


b = rndChoice(a)
print(b)


# ____________________________________________________________________________________________________
