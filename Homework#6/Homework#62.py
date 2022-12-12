# Exercise #2.2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def fill(a):
#     if a == 1:
#         return 1
#     else:
#         return a * fill(a-1)


# def nabor(elem):
#     result = []
#     for i in range(1, elem):
#         result.append(fill(i))
#     print(result)


# vvodnoe2 = int(input("Число для второй задачи: "))
# b = [fill(x) for x in range(1, vvodnoe2+1)]

# nabor(vvodnoe2)
# ____________________________________________________________________________________________________

# модернизация
def fill(a):
    if a == 1:
        return 1
    else:
        return a * fill(a-1)


vvodnoe2 = int(input("Число для второй задачи: "))

b = [fill(x) for x in range(1, vvodnoe2+1)]         # модернизация

print(b)
