from os import system
system("cls")


def print_finded(contact):
    print("Вот совпадение:")
    out = ""
    for elem in contact:
        out += str(elem)+" "
    print(out)
