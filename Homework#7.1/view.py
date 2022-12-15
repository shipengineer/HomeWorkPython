def init_book():
    with open('book.cvs', "r") as book:
        print("Ваш справочник")
        print("1 - посмотреть все контакты\n2 - найти контакт\n3 - добавить контакт\n4 - удалить контакт\n5 - экспортировать контакты\n6 - импортировать контакты")
        command = int(input("Введите номер команды: "))
        if command not in range(1, 6):
            init_book()
        else:
            return [command, book]


def view_contacts(data):
    print("Все контакты")
    for elem in data:
        print(elem + "\n")


def print_finded(data):
    for elem in data:
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


init_book()
