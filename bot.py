import telebot
import datetime
import threading # для ассинхронности

# Токен для доступа к боту
TOKEN = '8308029471:AAHrakR63QGHglWBcUHMRQiPZiuCmkh1_-k'

# Создаем экземпляр бота
# TeleBot is the main synchronous class for Bot.
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения данных всех пользователей
user_data = {}

# Создаем обработчики команд
@bot.message_handler(commands=['start'])
def send_message(message):

    # Формат текста именно такой, потому что иначе telegram
    # вставляет лишние пробелы в многострочное сообщение
    welcome_text = """
    Привет *★,°*:.☆(￣▽￣)/$:*.°★* 。*★.
    
Я - бот Remanda. Моя задача - напоминать тебе о всяких вещах, о которых стоило бы помнить, но ты обязательно забудешь 
    
ヽ(￣ω￣(￣ω￣〃)ゝ
    
Не волнуйся, браток, я готов тебе с этим помочь.
    
Введи /reminder ,  чтобы создать напоминалку
    """
    # Принимаем /start, возвращаем сообщение
    bot.send_message(message.chat.id, welcome_text)


# Функция для установки названия напоминания
@bot.message_handler(commands=['reminder'])
def reminder_name(message):
    bot.send_message(message.chat.id, 'Дай название своим детищам (oﾟvﾟ)ノ')

    #  bot.register_next_step_handler говорит, какая функция будет выполняться после ввода сообщения
    bot.register_next_step_handler(message, set_reminder_name)

# Функция для запоминания названия напоминания
def set_reminder_name(message):
    user_data[message.chat.id] = {'remainder_name': message}

    time_message = """
    А теперь дату и время напоминания в формате ГГГГ-ММ-ДД чч:мм:сс
    
Формат важен, потому что разраб пока не додумался до более красивого решения

(￣y▽,￣)╭ 
    """
    bot.send_message(message.chat.id, time_message)
    bot.register_next_step_handler(message, reminder_set, user_data)

# Функция для установки напоминания
def reminder_set(message):

    try:
        # Дата напоминания
        reminder_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
        # Дата сейчас
        now = datetime.datetime.now()
        delta = reminder_time - now

        # Контролируем, что пользователь вводит корректные дату и время по таймингу
        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, 'Похоже, ты глюпи и ввел прошедшую дату. Попробуй ещё раз ^_^')
        else:
            # Находим пользователя по chat.id => Находим название напоминания
            reminder = user_data[message.chat.id]['reminder']
            reminder_message = f'''
        Принято 
            
        d=====(￣▽￣*)b
            
        Твоя напоминалка "{reminder}" сработает {reminder_time}
            
            '''

            # Принимает delta.total_seconds, возвращает функцию send_reminder, которая принимает массив значений
            reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [message.chat.id, reminder_name])

            reminder_timer.start()
    except ValueError:

        yaix = '''
        Ой ( ఠ ͟ʖ ఠ)
        
    Кажется, формат ввода времени неправильный.
    Инструкции для тебя шутка какая-то???
    
    ಠ╭╮ಠ
    
    Переделывай давай. Потом на бедного разраба будут гнать.
        '''

        bot.send_message(message, yaix)



# Функция, которая отправляет сообщение с напоминанием
def send_reminder(chat_id, name):
    bot.send_message(chat_id, 'Напоминание ^-^. Получи и распишись:\n\n"{}"'.format(name))


@bot.message_handler(func=lambda message: True)
def other_messages(message):
    send_other = '''
    Извини. Я глюпи и не умею ничего, кроме отправки твоих глюпи напоминалок.
    
^_____^

Введи /reminder, чтобы создать напоминалку
    '''
    bot.send_message(message, send_other)


if __name__ == '__main__':
    print('Запуск успешен')
    bot.polling()