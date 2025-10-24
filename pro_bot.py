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

# Парсинг относительного времени "через Х минут сделай то-то"
def parse_relative_time(text):
    patterns = [
        r'через\s+(\d+)\s+([а-я]+)\s+(.+)',
        r'\s+(\d+)\s+([а-я]+)\s+(.+)',
        r'напомни\s+через\s+(\d+)\s+([а-я]+)\s+(.+)'
    ]

    time_units = {
        re.compile('сек'): 1,
        re.compile(r'мин'): 60,
        re.compile(r'час'): 3600,
        re.compile(r'дн'): 86400,
        re.compile(r'нед'): 604800,
        re.compile(r'мес'): 2592000,
    }

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            # Выделяем время и текст напоминания
            time_when = int(match.group(1))
            unit = match.group(2)
            reminder_text = match.group(3).split()

            # Находим множитель для единицы времени
            multiplier = None
            for unit_key, unit_mult in time_units.items():
                if unit_key.search(unit):
                    multiplier = unit_mult
                    break

            # Устанавливаем время в секундах, через сколько напоминать
            if multiplier:
                time_delta = datetime.timedelta(seconds=time_when * multiplier)
                return time_delta, reminder_text
    return None


# Парсинг абсолютного времени "в 18:00 завтра"
def parse_absolute_time(text):
    now = datetime.datetime.now()
    days_of_week = {
        ('понедельник', 'в понедельник'): 0,
        ('вторник', 'во вторник'): 1,
        ('среда', 'в среду'): 2,
        ('четверг', 'в четверг'): 3,
        ('пятница', 'в пятницу'): 4,
        ('суббота', 'в субботу'): 5,
        ('воскресенье', 'в воскресенье'): 6,
    }

    # Для слова "завтра"
    if 'завтра' in text:
        target_date = now.date() + datetime.timedelta(days=1)
        time_match = re.search(r'(\d{1, 2})[:\s]?(\d{2})?]', text)
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2) or 0)
            reminder_time = datetime.datetime.combine(target_date, datetime.time(hour, minute))
            reminder_text = re.sub(r'(завтра|в\s+\d{1,2}[:\s]?\d{0,2})', '', text)
            return reminder_time, reminder_text

    for day_name, day_num in days_of_week.items():
        if day_name in text:
            days_ahead = day_num - now.weekday() # Сколько дней осталось до нужного дня недели
            if days_ahead <= 0: # Если получилось отрицательное число, то точно больше недели осталось
                days_ahead += 7
            target_date = now.date() + datetime.timedelta(days=days_ahead)
            time_match = re.search(r'(\d{1, 2})[:\s]?(\d{2})?]', text)
            if time_match:
                hour = int(time_match.group(1))
                minute = int(time_match.group(2) or 0)
                reminder_time = datetime.datetime.combine(target_date, datetime.time(hour, minute))
                reminder_text = re.sub(r'(завтра|в\s+\d{1,2}[:\s]?\d{0,2})', '', text)
                return reminder_time, reminder_text
    return None, None

# Обработка естественного языка пользователя
@bot.message_handler(func=lambda message: True)
def handler_language(message):
    text = message.text
    chat_id = message.chat.id
    reminder_text, reminder_time = True



if __name__ == '__main__':
    print('Бот начал работу')
    bot.polling()