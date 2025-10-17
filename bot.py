import telebot
import datetime
import threading # для ассинхронности

# Токен для доступа к боту
TOKEN = '8308029471:AAHrakR63QGHglWBcUHMRQiPZiuCmkh1_-k'

# Создаем экземпляр бота
# TeleBot is the main synchronous class for Bot.
bot = telebot.TeleBot(TOKEN)

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


if __name__ == '__main__':
    print('Запуск успешен')
    bot.polling()