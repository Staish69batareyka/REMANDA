import telebot
from telebot.types import (KeyboardButton,  # Класс для создания кнопки
                           ReplyKeyboardMarkup, # Класс для создания клавиатуры
                           ReplyKeyboardRemove) # Класс для скрытия клавиатуры
import threading
import datetime
import re # Для регулярных выражений
import time # Для низкоуровневой работы со временем
from enum import Enum # Для работы с перечислениями = именованными константами

from bot import user_data

# (просто улучшает читабельность, синтаксический сахар)

TOKEN = '8308029471:AAHrakR63QGHglWBcUHMRQiPZiuCmkh1_-k'
bot = telebot.TeleBot(TOKEN)


# Обозначение типа чата
class ChatType(Enum):
    PRIVATE = 'private',
    GROUP = 'group'


# Словарь для определения временных интервалов
TIME_UNIT = {
    ('cек', ' c '): 1,
    'мин': 60,
    ('час', ' ч '): 3600,
    ('дн', 'день', ' д '): 86400,
    'нед': 604800,
    ('мес', ' м '): 2592000,
}

# Хранилище данных (пока так. Потом мб надо будет подключить какую-нить базу данных)
users_data = {}
group_data = {}


def create_menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        KeyboardButton('Создать напоминалку'),
        KeyboardButton('Мои напоминалки'),
        KeyboardButton(''),
        KeyboardButton(''),
    ]
    menu.add(*buttons[:2])
    menu.add(*buttons[2:])
    return menu

# Функция /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot_start_message = '''
    Привет *★,°*:.☆(￣▽￣)/$:*.°★* 。*★.

Я - бот Remanda. Моя задача - напоминать тебе о всяких вещах, о которых стоило бы помнить, но ты обязательно забудешь 

ヽ(￣ω￣(￣ω￣〃)ゝ

Не волнуйся, браток, я готов тебе с этим помочь.

Ещё я достаточно умный. Так что можешь написать в любом формате сообщение о напоминании. Что-то вроде "Завтра в 14:00 встреча" или "Мне нужно лечь спать в 8 утра". Я тебя пойму.

Используй кнопки и оцени все мои функции.
    '''
    bot.send_message(message.chat.id, bot_start_message, reply_markup=create_menu())


@bot.message_handler(func=lambda message: message.text == 'Создать напоминалку')
def create_reminder(message):
    bot.send_message(message.chat.id, 'Чего ты хочешь от меня?')


# Парсинг сообщения и извлечение названия и времени напоминания
def parse_reminder_text(text):
    to_lowercase = text.lower()

    # Относительное время

    # Абсолютное время

    return


# Обработка естественного языка пользователя
@bot.message_handler(func=lambda message: True)
def handler_language(message):
    text = message.text
    chat_id = message.chat.id
    reminder_text, reminder_time = True



if __name__ == '__main__':
    print('Бот начал работу')
    bot.polling()