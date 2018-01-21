import telebot
import constants

bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start','/stop')
    user_markup.row('фото', 'аудио')
    user_markup.row('стикеры', 'документы')
    bot.send_message(message.from_user.id,'Добро пожаловать ...',reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,"..",reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    



"""
#bot.send_message(244516180, "Hello!")

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]

#message_from_user = last_upd.message
#print(message_from_user)


@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print("Пришла команда")

print(bot.get_me())


def log(message, answer):
    print("\n--------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0}{1}. (id =  {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)
"""
"""
@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id,""Мои возможности весьма специфичны ! Но ты только посмотри !"")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Ты не умеешь играть в эту игру"
    if message.text == "а":
        answer = "Б"
        log(message,answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "б":
        answer = "В"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id, "Ну это 1 или 2 .....")
    elif message.text == "?" and str(message.from_user.id) == "244516180":
        bot.send_message(message.chat.id, "Ты избранный Нео!")
    else :
        bot.send_message(message.chat.id, answer)
        log(message, answer)
"""
"""
@bot.message_handler(content_types=["document"])
def handle_command(message):
    print("Пришел документ")

@bot.message_handler(content_types=["audio"])
def handle_command(message):
    print("Пришла аудиозапись")

@bot.message_handler(content_types=["photo"])
def handle_command(message):
    print("Пришло фото")

@bot.message_handler(content_types=["sicker"])
def handle_command(message):
    print("Пришел стикер")
"""

bot.polling(none_stop=True)