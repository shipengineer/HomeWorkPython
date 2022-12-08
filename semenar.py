# # 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# # ['ssss', 'sngujn556', 56] -> Yes
# # ['56', 'sgnbsb'] -> No

# spisok1 = ['jhfhf', 123, "12334333", 11]
# spisok2 = ['jhfhf', "123", "12334333", "11"]


# def proverkaNaDigit(listing):
#     for i in range(len(listing)):
#         a = listing[i]
#         # print(type(a))
#         j = 0
#         if type(a) == int:
#             print("Yes")
#             j += 1
#             break
#     if j == 0:
#         print("No")


# proverkaNaDigit(spisok2)

# # 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# # ​
# # *Пример:*
# # ​
# # - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# # - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# # - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# # - список: [], ищем: "123", ответ: -1

# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# list4 = ["123", "234", 123, "567"]
# list5 = []

# find1 = "qwe"
# find2 = "йцу"
# find3 = "йцу"
# find4 = "123"
# find5 = "123"


# def Find(find, list):
#     count = 0
#     for i in range(len(list)):
#         if find == list[i]:
#             count += 1
#             if count == 2:
#                 return i
#     if count <= 1:
#         return (-1)


# # result1 = Find(find1, list1)
# print(f'Позиция: {Find(find1, list1)}')

# result2 = Find(find2, list2)
# print(f'Позиция: {result2}')

# result3 = Find(find3, list3)
# print(f'Позиция: {result3}')

# result4 = Find(find4, list4)
# print(f'Позиция: {result4}')

# result5 = Find(find5, list5)
# print(f'Позиция: {result5}')

# for i in range(5):
#     Find('find'+i, 'list'+i)

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# number = input('Введите число: ').split()
# mass = []

# for i in range(len(number)):
#     mass.append(int(number[i]))
# print(mass)

# max = mass[0]
# min = mass[0]
# for i in range(len(mass)):
#     if mass[i] > max:
#         max = mass[i]
#     if mass[i] < min:
#         min = mass[i]

# print(f' Максимальное число: {max}')
# print(f' Минимальное число: {min}')

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


# from sympy.solvers import solve
# from sympy import Symbol


# def roots(a, b, c):
#     D = 0
#     D = b**2 - 4 * a*c
#     if D < 0:
#         print("Нет корней")
#     elif D == 0:
#         x1 = -b/(2*a)
#         print(x1)
#     elif D > 0:
#         x1 = (-b + D**0.5)/(2 * a)
#         x2 = (-b - D**0.5)/(2 * a)
#         print(x1, x2)


# def rootsSymPy(a, b, c):
#     x = Symbol('x')
#     print(solve(a*x**2+b*x+c, x))


# rootsSymPy(2, 6, 9)


# def NOD(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return (a+b)


# def NOK(first, second):
#     print(f'Наименьшее общее кратное = {first*second/NOD(first, second)}')
#     return ((first*second/NOD(first, second)))


# NOK(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
