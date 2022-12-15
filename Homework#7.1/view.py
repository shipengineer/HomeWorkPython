def init_book():
    print("Ваш справочник")
    print("1 - посмотреть все контакты\n2 - найти контакт\n3 - добавить контакт\n4 - удалить контакт\n5 - экспортировать контакты\n6 - импортировать контакты")
    return input("Введите номер команды: ")


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


def delete_contact_ID():
    return input("Укажите ID контакта на удаление")


def export_question():
    amount = input("Укажите ID котактов на экспорт")
    format = input(
        "Укажите формат вывода данных.\n Доступные форматы вывода: xml, csv")
    return [amount, format]


init_book()
