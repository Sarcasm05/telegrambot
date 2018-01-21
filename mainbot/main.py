import telebot
import constants

bot = telebot.TeleBot(constants.token)


def log(message, answer):
    print("\n--------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0}{1}. (id =  {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Начать работу')
    user_markup.row('Посмотреть соцсети')
    bot.send_message(message.from_user.id,'Добро пожаловать, начнем зарабатывать?',reply_markup=user_markup)

@bot.message_handler(commands=['social'])
def handle_social(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Youtube','Twitter')
    user_markup.row('VK', 'Instagram')
    bot.send_message(message.from_user.id,'Чекни наши соцсети : ',reply_markup=user_markup)

@bot.message_handler(commands=['task'])
def handle_task(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('задание 1', 'задание 2')
    user_markup.row('задание 3', 'задание 4')
    user_markup.row('Выход')
    bot.send_message(message.from_user.id,'Выберите задание : ',reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты не умеешь играть в эту игру"
    if message.text == "Youtube":
        answer = "www.youtube.com"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Twitter":
        answer = "twitter.com"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "VK":
        answer = "vk.com"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Instagram":
        answer = "instagram.com"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Выбрать задание":
        answer = "Пример задания или ссылка на него"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Посмотреть соцсети":
        handle_social(message)
        #log(message,answer)
        bot.send_message(message.chat.id, answer)
    else :
        answer = "Даже не знаю что вам ответить"
        #log(message,answer)
        bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
     bot.polling(none_stop=True)