from random import randint, choice
from telebot import types
import telebot
token = "5781156725:AAGtzXHixt3gURowz73mJ8nxUtPbvm63cX4"
bot = telebot.TeleBot(token)
vase = dict()
turn = dict()
game = dict()
game_mode = dict()
order = dict()


def check_win(message):
    global game, order
    if vase[message.chat.id] <= 28:
        if game_mode[message.chat.id] == 'pvp':
            bot.send_message(
                message.chat.id, f"Победил игрок № {1 if turn else 2}")
            game[message.chat.id] = False
        if game_mode[message.chat.id] == 'pve':
            bot.send_message(
                message.chat.id, f"Выйграл {'Человек' if order[message.chat.id]==1 else 'Бот'}")
            game[message.chat.id] = False


def new_game(message):
    global game, vase, turn
    game[message.chat.id] = True
    vase[message.chat.id] = 56
    turn[message.chat.id] = choice([True, False])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Новая игра")
    item2 = types.KeyboardButton("Игра против игрока")
    item3 = types.KeyboardButton("Игра против бота")
    markup.add(item2, item3)
    markup.add(item1)

    bot.send_message(message.chat.id, 'Начнем игру?',
                     reply_markup=markup)

# Здесь я решил не изобретать велосипед. Насколько я понял, мы обрабатываем вводимое
# что бы в полседуещем ввести его в функцию игры


def handle_game_proc(message):
    global game
    try:
        if game[message.chat.id] and 1 <= int(message.text) <= 28:
            print('100')
            return True
        else:
            print('101')
            return False
    except KeyError:
        game[message.chat.id] = False
        if game[message.chat.id] and 1 <= int(message.text) <= 28:
            print('102')
            return True
        else:
            print('103')
            return False


@bot.message_handler(content_types='text')
def message_reply(message):
    global game_mode
    if message.text == "Новая игра":
        new_game(message)
        bot.send_message(
            message.chat.id, "Начнем новую игру")

    if message.text == "Игра против игрока":
        new_game(message)
        game_mode[message.chat.id] = 'pvp'
        bot.send_message(
            message.chat.id, f"Тянет игрок номер {1 if turn[message.chat.id] else 2}")

    if message.text == "Игра против бота":
        new_game(message)
        game_mode[message.chat.id] = 'pve'
        bot.send_message(
            message.chat.id, f"Тянет {'Человек' if turn[message.chat.id] else 'Бот'}")
        if not (turn[message.chat.id]):
            hand = randint(1, 29)
            vase[message.chat.id] -= hand
            bot.send_message(
                message.chat.id, f"Бот вытянул {hand}")
            bot.send_message(
                message.chat.id, f"в вазе осталось {vase[message.chat.id]} конфет")
            bot.send_message(
                message.chat.id, f"Тянет человек")
            check_win(message)
            turn[message.chat.id] = not (turn[message.chat.id])

    else:
        game_run(message)


def game_run(message):
    global game, vase, turn, game_mode, order
    check_win(message)
    if 1 <= int(message.text) <= 28 and game[message.chat.id]:

        if game_mode[message.chat.id] == 'pvp' and game_mode[message.chat.id]:

            vase[message.chat.id] -= int(message.text)
            bot.send_message(
                message.chat.id, f"в вазе осталось {vase[message.chat.id]} конфет")
            turn[message.chat.id] = not (turn[message.chat.id])
            bot.send_message(
                message.chat.id, f"Теперь тянет игрок №{1 if turn[message.chat.id] else 2} ")

        if game_mode[message.chat.id] == 'pve' and game_mode[message.chat.id]:

            if turn[message.chat.id]:
                order[message.chat.id] = 0
                vase[message.chat.id] -= int(message.text)
                bot.send_message(
                    message.chat.id, f"Человек вытянул {message.text}")
                bot.send_message(
                    message.chat.id, f"в вазе осталось {vase[message.chat.id]} конфет")

                bot.send_message(
                    message.chat.id, f"Теперь тянет Бот ")
                if vase[message.chat.id] > 28:
                    hand = randint(1, 29)
                    vase[message.chat.id] -= hand
                    bot.send_message(
                        message.chat.id, f"Бот вытянул {hand}")
                    bot.send_message(
                        message.chat.id, f"в вазе осталось {vase[message.chat.id]} конфет")
                    bot.send_message(
                        message.chat.id, f"Тянет человек")
                    order[message.chat.id] = 1

    elif game[message.chat.id]:
        bot.send_message(
            message.chat.id, f"Ты идиот? только цифры и от 0 до 28")
    check_win(message)


bot.infinity_polling()
