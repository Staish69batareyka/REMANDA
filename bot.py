import telebot

# Токен для доступа к боту
TOKEN = '8308029471:AAHrakR63QGHglWBcUHMRQiPZiuCmkh1_-k'

# Создаем экземпляр бота
# TeleBot is the main synchronous class for Bot.
bot = telebot.TeleBot(TOKEN)

# Создаем обработчики команд
@bot.message_handler(commands=['start'])
def send_message(message):
    # Принимаем /start , возвращаем сообщение
    bot.send_message(message.chat.id, 'Привет ^^/ . Я - твое эхо. Скажи что-нибудь - я повторю')


# Обработчик любого сообщения, которое прислали, чтобы повторить его

# Параметр func= создает условия для выполнения,
# lambda обозначает, что мы создаем маленькую функцию в 1 строку
# message: True - параметр функции и возвращаемое значение

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    print('Запуск успешен')
    bot.polling()