def init_book(file):
    base = []
    out = []
    with open(file, "r") as file:
        base = file.readlines()
        for elem in base:
            out.append(elem.split())
    return out


def main_menu():
    print("Ваш справочник")
    print("1 - посмотреть все контакты\n2 - найти контакт\n3 - добавить контакт\n4 - удалить контакт\n5 - экспортировать контакты\n6 - импортировать контакты")
    command = int(input("Введите номер команды: "))
    if command not in range(1, 6):
        main_menu()
    else:
        return command


book = init_book('phonebase.txt')
print(book)


def view_contacts(book):
    print("Все контакты:")
    for person in book:
        for key in person:
            print(key)
        print("\n")


view_contacts(book)


def print_finded(book):
    for elem in book:
        print("Вот совпадение:")
        out = ""
        for key, value in elem:
            out = + (key + ':' + value+' ')
        print(out + '\n')


def create_contact_input():
    return input("Укажите данные новой записи в следующем порядке: Имя Фамилия Телефон Эл.Почта\n Через пробел, пожалуйста: ")


def delete_contact_print():
    return input("Укажите ID контакта на удаление")


def export_question():
    IDs = input("Укажите ID котактов на экспорт.\n Через пробел, пожалуйста:")
    return IDs


def import_qestion():
    return input("Укажите файл импорта:")
