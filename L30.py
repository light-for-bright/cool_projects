# my_token = 'XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

import telebot
from telebot import types
from config import my_token
import random

bot = telebot.TeleBot(my_token)

anecdot_list = []
an1 = 'анекдот1'
an2 = 'анекдот2'
an3 = 'анекдот3'
anecdot_list.append(an1)
anecdot_list.append(an2)
anecdot_list.append(an3)

# Команда для запуска: /start


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Я твой первый бот')
    # print(message.text)


def add_task(message):
    delo = message.text
    with open('spisok_del_2.txt', 'a', encoding='utf-8') as file:
        file.write(delo + '\n')
    bot.send_message(message.chat.id, f"✅ Добавлено!")


@bot.message_handler(content_types='text')
def send_everything(message):
    if message.text == 'Добавить дело':
        msg = bot.send_message(message.chat.id, 'Что добавить?')
        bot.register_next_step_handler(msg, add_task)

    elif message.text == 'Посмотреть список дел':
        bot.send_message(message.chat.id, 'У меня тоже)')
        answ = random.choice(anecdot_list)
        bot.send_message(message.chat.id, answ)

    else:
        buttons = types.ReplyKeyboardMarkup(row_width=1)
        but1 = types.KeyboardButton('Добавить дело')
        but2 = types.KeyboardButton('Посмотреть список дел')
        buttons.add(but1, but2)
        bot.send_message(message.chat.id, 'Выбери: ', reply_markup=buttons)
        # print(message.text)


bot.infinity_polling()
