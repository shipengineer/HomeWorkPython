import view as vw


def get_base(file_name):
    base = []
    out = []
    with open(file_name, "r") as file:
        base = file.readlines()
        for elem in base:
            out.append(elem.split())
    return out


# path = "Homework#1\\Homework#7.2\\"
# book = get_base(path+"phonebase.txt")


def get_person(base):
    global vm
    find_item = input('Над кем работаем, или кого просто, ищем?: ')
    for person in base:
        lowercase = []
        for elem in person:
            lowercase.append(str(elem).lower())

        if find_item.lower() in lowercase:
            vw.print_finded(person)


def delete_person(base):
    get_person(base)
    find_item = input('Введите ID, которое нужно удалить: ')
    for person in base:
        if find_item in person:
            base.remove(person)


def add_person(base):
    id = int(base[len(base)-1][0])+1
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone_number = input('Введите телефон: ')
    email = input('Введите email: ')
    description = input('Введите описание: ')
    base.append([id, name, last_name, phone_number, email, description])


def edit_person(base):
    get_person(base)
    id = input('Введите id, кого исправляем: ')
    for person in base:
        if id in person:
            command = input(
                "Введите номер команды(1 - изменить имя, 2 - изменить фамилию, 3 - изменить телефон,4 - ищменить email, 5 - изменить описание): ")
            match command.split():
                case ["1"]: person[1] = input('Введите новое имя: ')
                case ["2"]: person[2] = input('Введите новую фамилию: ')
                case ["3"]: person[3] = input('Введите новый телефон: ')
                case ["4"]: person[4] = input('Введите новый email: ')
                case ["5"]: person[5] = input('Введите новое описание: ')

                case unknown_command: print(f"Command '{command}' not understood")


def save_base(base):
    path = "Homework#1\\Homework#7.2\\"

    with open(path+(input("Укажите файл в который записываем или нажмите Enter") or "phonebase.txt"), "w") as file:
        for elem in base:
            out = ""
            for item in elem:
                out += str(item)+" "
            file.write(f"{out}\n")
