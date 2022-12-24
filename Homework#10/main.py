from telebot import types
import telebot
import urllib.request
import bs4 as bs

token = "5886220402:AAE017J30m8eVB94G5-YwItyV8cLqSrkmWU"
bot = telebot.TeleBot(token)

# Создание супца
sauce = urllib.request.urlopen(
    'https://www.cbr-xml-daily.ru/daily_utf8.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')

# Функция извлечения данных


def convert(source):
    valute_nominal = []
    valute_name = []
    valute_cur_rub = []

    for info in source.find_all('Nominal'):
        valute_nominal.append(info.text)

    for info in source.find_all('Name'):
        valute_name.append(info.text)

    for info in source.find_all('Value'):
        valute_cur_rub.append(info.text)

    currency = list(zip(valute_nominal, valute_name, valute_cur_rub))
    # currency[0] = номинал валюты , currency[1] = Имя валюты, currency[2] = курс в рублях
    return currency


# Фронт бота
base = convert(soup)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for elem in base:
        markup.add(types.InlineKeyboardButton(f'{elem[1]}'))
    bot.send_message(
        message.chat.id, 'Готов предоставить вам курсы валют\nУкажите какая валюта вас интересует', reply_markup=markup)


@bot.message_handler(content_types='text')
def reply_currency(message):
    for elem in base:
        if message.text in elem:
            bot.send_message(
                message.chat.id, f'Курс {elem[0]} {elem[1]} составляет {elem[2]} рублей')


bot.infinity_polling()
