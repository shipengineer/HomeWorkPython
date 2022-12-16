import model as ml
import view as vw
from pathlib import Path

book = ml.get_base("phonebase.txt")


def main_menu():
    print("Ваш справочник:\nКоманды:\n1-найти контакт\n2-удалить контакт\n3-добавить контак\n4-изменить контакт\n5-сохранить книгу\n6-импортировать книгу")
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: ml.get_person(book)
        case ["2"]: ml.delete_person(book)
        case ["3"]: ml.add_person(book)
        case ["4"]: ml.edit_person(book)
        case ["5"]: ml.save_base(book)
        case ["6"]: ml.get_base(
            input("Укажите имя файла в импортирования контактов"))
        case unknown_command: print(f"Command '{command}' not understood")
    print("\n")
    main_menu()


main_menu()
