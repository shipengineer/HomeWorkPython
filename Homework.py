# ----------------------------------Exercise #1------------------------------
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# ----------------------------------SOLUTION-----------------------------------
# def holydays():
#     a = int(input("впишите день недели "))
#     if a == 6 or a == 7:
#         print(f"{a} -> да")
#     elif 0 < a < 6:
#         print(f"{a} -> нет")
#     else:
#         print(f"{a} -> введен не день недели")
#         holydays()


# holydays()

# ----------------------------------Exercise #1------------------------------
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
fExpression = input("Первая предитата = ")
sExpression = input("Вторая предитата = ")
trdExpression = input("Тертья предитата = ")


def logicCheck(X, Y, Z):
    firstHalf = X or Y or Z
    secondHalf = not X and not Y and not Z
    check = not firstHalf == secondHalf
    print(check)


logicCheck(fExpression, sExpression, trdExpression)
