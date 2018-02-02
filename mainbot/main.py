import sqlite3
import telebot
import constants
from botnet.pyTelegramBotAPI.telebot import types


bot = telebot.TeleBot(constants.token)

def autorisation(message):
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')
    # print(c.fetchall())
    flagrow = False
    for row in c:
        id_number = row[0]
        # print(row[0])
        if id_number == message.chat.id:
            # print(message.chat.id)
            # print('\n message chat id = ',message.from_user.id)
            # bot.send_message(message.chat.id, "Вы есть в базе данных!")
            flagrow = True
    c.close()
    return flagrow


@bot.message_handler(commands=['regist'])
def add_user(message):
    if autorisation(message) == False:
        conn = sqlite3.connect('base')
        c = conn.cursor()
        # (id, first_name, username, task_id, number_task, id_wallet, money, number_ballov, rang, level)
        user = [message.chat.id, 0, 0, 0, 0, 0, 0, 0]
        c.execute('INSERT INTO users VALUES (%s)' % ','.join('?' * len(user)), user)
        conn.commit()
        c.close()
    else:
        bot.send_message(message.chat.id, "Нечего беспокоиться , вы уже есть в базе!")


#bot.remove_webhook()
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Начать работу')
    user_markup.row('Посмотреть соцсети')
    bot.send_message(message.from_user.id,'Добро пожаловать, начнем зарабатывать?',reply_markup=user_markup)

@bot.message_handler(commands=['social'])
def handle_social(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Twitter', url='https://twitter.com/W0rldBlockchain')
    markup.add(btn_my_site)
    btn_my_site = types.InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/channel/UC4pqIogmWRtSD4l8Ikc5Itg')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Наши соцсети:", reply_markup=markup)

"""
@bot.message_handler(commands=["phone"])
def getphone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    #button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Для начала нужно ввести номер телефона:", reply_markup=keyboard)


@bot.message_handler(commands=['task'])
def get_task(message):
    markup = types.InlineKeyboardMarkup()
    #text1 = "Махачкала — город на юге России, на Кавказе, на берегу Каспийского моря, столица Дагестана,третий по численности населения город Северо-Кавказского региона и крупнейший город Северо-Кавказского федерального округа. Образует городской округ город Махачкала. Является ядром почти миллионной Махачкалинско-Каспийской агломерации."
    btn_my_site = types.InlineKeyboardButton(text= 'Задание Махачкала', callback_data = "task1")
    markup.add(btn_my_site)
    btn_my_site = types.InlineKeyboardButton(text='Задание Москва', callback_data="task2")
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Список доступных тебе заданий :", reply_markup=markup)
"""


def get_task(message):
    #bot.send_message(message.chat.id, "Выбери задание : ")
    conn = sqlite3.connect('tasks_base')
    c = conn.cursor()
    c.execute('select * from tasks order by id')
    markup = types.InlineKeyboardMarkup()
    for row in c:
        btn_my_task = types.InlineKeyboardButton(text = row[1], callback_data= row[0])
        markup.add(btn_my_task)
    bot.send_message(message.chat.id, "Список доступных тебе заданий : ", reply_markup=markup)
    c.close()

@bot.message_handler(commands=['money'])
def get_ballance(message):
    if autorisation(message) == True:
        conn = sqlite3.connect('base')
        c = conn.cursor()
        c.execute('select * from users order by id')
        for row in c:
            if row[0] == message.chat.id:
                money = row[4]
                bot.send_message(message.chat.id, "{0}, Ваш балланс = {1} монет".format(message.chat.first_name, money))
                c.close()
                break
    else:
        add_user(message)
        bot.send_message(message.chat.id, "{0}, Ваш балланс = 0 монет".format(message.chat.first_name))

def keybord_accept_task(call):
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row('Принять задание')
    markup.row('Выбрать заного')
    bot.send_message(call.message.chat.id, text= None, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    # Если сообщение из чата с ботом
    if call.message:
        conn = sqlite3.connect('tasks_base')
        c = conn.cursor()
        c.execute('select * from tasks order by id')
        for row in c:
            if call.data == str(row[0]):
                task = row[2]
                bot.send_message(call.message.chat.id, "За это задание ты получишь {0} балл(a/ов)".format(row[3]))
                keybord_accept_task(call)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=task)

                if handle_acception(call.message) == True:
                    pass
                    #добавить в бд в столбец монетки количество баллов за задание
                else:
                    pass
                    #Начать заного
                    #get_task(call.message)
                c.close()
                break

    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        conn = sqlite3.connect('tasks_base')
        c = conn.cursor()
        c.execute('select * from tasks order by id')
        for row in c:
            if call.data == row[0]:
                task = row[2]
                bot.edit_message_text(inline_message_id=call.inline_message_id, text=task)
                c.close()
                break

#@bot.message_handler(content_types=['text'])
def handle_acception(message):
    if message.text == 'Принять задание':
        return True
        #Принимаем задание и добавляем пользователю токен
    elif message.text == 'Выбрать заного':
        return False
        #Показать список заданий заного

@bot.message_handler(content_types=['text'])
def handle_text(message):
    phone_number = False
    answer = "Даже не знаю что вам ответить"
    if message.text == "Посмотреть соцсети":
        handle_social(message)
        #log(message,answer)
        #bot.send_message(message.chat.id, answer)
    elif message.text == "Начать работу":
        #answer = 'Доступные вам задания:'
        flagrow = autorisation(message)
        if flagrow == False:
            add_user(message)
            get_task(message)
        else:
            #print("есть в базе")
            get_task(message)
    else:
        bot.send_message(message.chat.id, "Напиши чет дельное уже, заебал , нет такой команды!")

if __name__ == '__main__':
     bot.polling(none_stop=True)