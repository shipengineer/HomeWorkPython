from os import system
system("cls")


def print_finded(contact):
    print("Вот совпадение:")
    out = ""
    for elem in contact:
        out += str(elem)+" "
    print(out)



def print_table(data):
    columns = ['ID', 'Имя', 'Фамилия', 'Должность', 'Номер Телефона', 'e-mail']
    max_columns = []  # список максимальной длинны колонок
    for col in zip(*data):
        len_el = []
        [len_el.append(len(el)) for el in col]
        max_columns.append(max(len_el))
    # печать таблицы с колонками максимальной длинны строки
    # печать шапки таблицы
    for column in columns:
        print(f'{column:{max(max_columns)+1}}', end='')
    print()
    # печать разделителя шапки
    print(f'{"="*max(max_columns)*5}')
    # печать тела таблицы
    for el in data:
        for col in el:
            print(f'{col:{max(max_columns)+1}}', end='')
        print()
