import model as ml
import view as vw

path = "Homework#1\\SEM_08.py\\"
book = ml.get_base(path+"data_base.csv")


def main_menu():
    print("Ваш справочник:\nКоманды:\n1-найти сотрудника\n2-удалить запись о сотруднике\n3-добавить запись о сотруднике\n4-изменить информацию о сотруднике\n5-сохранить список сотрудников\n6-импортировать журнал сотрудников\n7-показать весь перечень\n8-выйти из книги")
    command = input("Введите номер команды: ")
    match command.split():
        case ["1"]: ml.get_person(book)
        case ["2"]: ml.delete_person(book)
        case ["3"]: ml.add_person(book)
        case ["4"]: ml.edit_person(book)
        case ["5"]: ml.save_base(book)
        case ["6"]: ml.get_base(
            input("Укажите имя файла в импортирования журнала"))
        case ["7"]: vw.print_table(book)
        case ["8"]: ml.save_base(book); print("Всего наилучшего"); raise SystemExit
                   
        case unknown_command: print(f"Command '{command}' not understood")
    print("\n")
    main_menu()
