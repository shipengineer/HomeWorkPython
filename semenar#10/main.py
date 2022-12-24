import requests
import urllib.request
import bs4 as bs


sauce = urllib.request.urlopen(
    'https://www.cbr-xml-daily.ru/daily_eng_utf8.xml').read()
soup = bs.BeautifulSoup(sauce, 'html')
print(soup)


def convert(source):

    result = []
    for elem in source:
        out = []
        out.append(elem['Nominal'])
        out.append(elem.Name)
        out.append(elem.Value)
        result.append(out)
    return result


# def print_table(data):
#     columns = ['Номинал', 'Имя Валюты', 'Курс']
#     max_columns = []  # список максимальной длинны колонок
#     for col in zip(*data):
#         len_el = []
#         [len_el.append(len(el)) for el in col]
#         max_columns.append(max(len_el))
#     # печать таблицы с колонками максимальной длинны строки
#     # печать шапки таблицы
#     for column in columns:
#         print(f'{column:{max(max_columns)+1}}', end='')
#     print()
#     # печать разделителя шапки
#     print(f'{"="*max(max_columns)*5}')
#     # печать тела таблицы
#     for el in data:
#         for col in el:
#             print(f'{col:{max(max_columns)+1}}', end='')
#         print()

# print(convert(soup))
# # print_table(convert(soup))

# resp = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()

# print(resp['Valute']['USD']['Value'])

# resp = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
# print(resp['Valute']['USD']['Value'])
