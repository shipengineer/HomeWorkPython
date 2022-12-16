from os import system
system("cls")

def get_base():
    base = []
    out = []
    file_file = 'file.txt'
    with open(file_file, "r") as file:
        base = file.readlines()
        for elem in base:
            out.append(elem.split())
    return out
book = get_base()


def get_person(base):
    find_item = input('Введите имя: ')
    for person in base:
        if find_item in person:
            print(person)
# get_person(book)

def main_menu():
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: print("X --> от 0 до + ꝏ; Y --> от 0 до + ꝏ")  
        case ["2"]: print("X --> от 0 до + ꝏ; Y --> от 0 до - ꝏ")
        case ["3"]: print("X --> от 0 до - ꝏ; Y --> от 0 до - ꝏ")
        case ["4"]: print("X --> от 0 до - ꝏ; Y --> от 0 до + ꝏ")
        case unknown_command: print (f"Command '{command}' not understood")

def delit_person(base):
    get_person(base)
    find_item = input('Введите ID, которое нужно удалить: ')
    for person in base:
        if find_item in person:
            base.remove(person)
# delit_person(book)
# print(book)

def add_person(base):
    id = base[len(base)-1][0]+1
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = input('Введите телефон: ')
    base.append([id,name,last_name,phone_number])
# add_person(book)
# print(book)

def edit_person(base):
    get_person(base)
    id = input('Введите id, кого исправляем: ')
    for person in base:
        if id in person:
            command = input("Введите номер команды(1 - изменить имя, 2 - изменить фамилию, 3 - изменить телефон): ")
            match command.split():
                case ["1"]: person[1] = input('Введите новое имя: ')
                case ["2"]: person[2] = input('Введите новое имя: ')
                case ["3"]: person[3] = input('Введите новое имя: ')
                case ["4"]: person[4] = input('Введите новое имя: ')
                case unknown_command: print (f"Command '{command}' not understood")
edit_person(book)
print(book)

def save_base(base):
    out = ""  
    with open('file.txt', "w") as file:
        for elem in base:
            for item in elem:
                out += str(item+" ")
                file.write("{out}+\n")
save_base(book)

