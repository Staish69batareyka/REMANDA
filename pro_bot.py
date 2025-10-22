import telebot
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
    'cек': 1,
    'мин': 60,
    'час': 3600,
    ('дн', 'день'): 86400,
    'нед': 604800,
    'мес': 2592000,
}

# Хранилище данных (пока так. Потом мб надо будет подключить какую-нить базу данных)
users_data = {}
group_data = {}



# Функция /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message, '''
    Привет *★,°*:.☆(￣▽￣)/$:*.°★* 。*★.

Я - бот Remanda. Моя задача - напоминать тебе о всяких вещах, о которых стоило бы помнить, но ты обязательно забудешь 

ヽ(￣ω￣(￣ω￣〃)ゝ

Не волнуйся, браток, я готов тебе с этим помочь.

Введи /reminder ,  чтобы создать напоминалку
    ''')


if __name__ == '__main__':
    print('Бот начал работу')
    bot.polling()