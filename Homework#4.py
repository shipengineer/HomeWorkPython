# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
import math


def roundPi(d):
    count = len(d)
    pi = str(math.pi)
    print(pi[:count])


# roundNumber = input("Укажите сколько знаков после запятой (Пример: 0.0001) : ")
# roundPi(roundNumber)
# ____________________________________________________________________________________________________

# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def SimpMult(num):
    result = [1]
    i = 2
    mutable = num
    while i <= num:
        if num % i == 0:
            if i not in result:
                result.append(i)

            num //= i
        else:
            i += 1
    print(f'Простые множители числа {mutable} : {result}')


# Nnum = int(input("Введите число для разложения на простые множители: "))
# SimpMult(Nnum)
