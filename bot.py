import telebot
import datetime
import threading

TOKEN = '8308029471:AAHrakR63QGHglWBcUHMRQiPZiuCmkh1_-k'
bot = telebot.TeleBot(TOKEN)
user_data = {}


@bot.message_handler(commands=['start'])
def send_message(message):
    welcome_text = """
    Привет *★,°*:.☆(￣▽￣)/$:*.°★* 。*★.

Я - бот Remanda. Моя задача - напоминать тебе о всяких вещах, о которых стоило бы помнить, но ты обязательно забудешь 

ヽ(￣ω￣(￣ω￣〃)ゝ

Не волнуйся, браток, я готов тебе с этим помочь.

Введи /reminder ,  чтобы создать напоминалку
    """
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['reminder'])
def reminder_name(message):
    bot.send_message(message.chat.id, 'Дай название своим детищам (oﾟvﾟ)ノ')
    bot.register_next_step_handler(message, set_reminder_name)


def set_reminder_name(message):
    # ✅ ИСПРАВЛЕНО: правильный ключ и message.text
    user_data[message.chat.id] = {'reminder_name': message.text}

    time_message = """
    А теперь дату и время напоминания в формате ГГГГ-ММ-ДД чч:мм:сс

Формат важен, потому что разраб пока не додумался до более красивого решения

(￣y▽,￣)╭ 
    """
    bot.send_message(message.chat.id, time_message)
    bot.register_next_step_handler(message, reminder_set, user_data)


def reminder_set(message, user_data):
    try:
        reminder_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        delta = reminder_time - now

        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, 'Похоже, ты глюпи и ввел прошедшую дату. Попробуй ещё раз ^_^. Жми /reminder')
        else:
            # ✅ ИСПРАВЛЕНО: правильный ключ
            reminder = user_data[message.chat.id]['reminder_name']
            reminder_message = f'''
        Принято 

d=====(￣▽￣*)b

Твоя напоминалка "{reminder}" сработает {reminder_time}

            '''
            # ✅ ИСПРАВЛЕНО: передаем chat_id, а не message
            bot.send_message(message.chat.id, reminder_message)

            # ✅ ИСПРАВЛЕНО: правильная переменная
            reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [message.chat.id, reminder])
            reminder_timer.start()

    except ValueError:
        yaix = '''
        Ой ( ఠ ͟ʖ ఠ)

Кажется, формат ввода времени неправильный.
Инструкции для тебя шутка какая-то???

ಠ╭╮ಠ

Переделывай давай. Потом на бедного разраба будут гнать.
Жми /reminder, чтобы отмыть позор
        '''
        # ✅ ИСПРАВЛЕНО: передаем chat_id
        bot.send_message(message.chat.id, yaix)


def send_reminder(chat_id, name):
    bot.send_message(chat_id, 'Напоминание ^-^. Получи и распишись:\n\n"{}"'.format(name))


@bot.message_handler(func=lambda message: True)
def other_messages(message):
    send_other = '''
    Извини. Я глюпи и не умею ничего, кроме отправки твоих глюпи напоминалок.

^_____^

Введи /reminder, чтобы создать напоминалку
    '''

    bot.send_message(message.chat.id, send_other)


if __name__ == '__main__':
    print('Запуск успешен')
    bot.polling()