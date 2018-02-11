import sqlite3
import telebot
import config
from keyboard_class import Keyboard
bot = telebot.TeleBot(config.token)


def status_task(message):
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')
    for row in c:
        if row[0] == message.from_user.id:
            status = row[2]
            print(status)
            if status == 'NO':
                return 'NO'
            elif status == 'EMPTY' :
                return 'EMPTY'
            else:
                return 'YES'
    c.close()


def cancel_task(message):
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')
    for row in c:
        if row[0] == message.from_user.id:
            row[2] = "EMPTY"
            break
    c.close()



def get_task(message):
    #bot.send_message(message.chat.id, "Выбери задание : ")
    
    conn = sqlite3.connect('tasks_base')
    c = conn.cursor()
    c.execute('select * from tasks order by id')
    for row in c:
        bot.send_message(message.from_user.id, row[1])
        bot.send_message(message.from_user.id, row[2])
        bot.send_message(message.chat.id, "За это задание ты получишь {0} монет(у)".format(row[3]))
        task_id = row[0]
        break
    c.close()
    
    '''
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')

    for row in c:
        if row[0] == message.from_user.id:
            row[1] = task_id
            row[2] = 'YES'
            break
    c.commit()
    c.close()
    '''



#Деньги (потом будут все атрибуты)
def get_ballance(message):
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')
    for row in c:
        if row[0] == message.chat.id:
            money = row[4]
            bot.send_message(message.chat.id,
                             "{0}, Ваш балланс = {1} монет".format(message.chat.first_name, money))
            c.close()
            break

#Проверка на регистрацию
def autorisation(message):
    conn = sqlite3.connect('base')
    c = conn.cursor()
    c.execute('select * from users order by id')
    flagrow = False
    for row in c:
        id_number = row[0]
        if id_number == message.chat.id:
            flagrow = True
    c.close()
    return flagrow

#Регистрация
def add_user(message):
    #if autorisation(message) == False:
    conn = sqlite3.connect('base')
    c = conn.cursor()
        # (id, first_name, username, task_id, number_task, id_wallet, money, number_ballov, rang, level)
    user = [message.chat.id, 0, 0, 0, 0, 0, 0, 0]
    c.execute('INSERT INTO users VALUES (%s)' % ','.join('?' * len(user)), user)
    conn.commit()
    c.close()
    #else:
    #    bot.send_message(message.chat.id, "Нечего беспокоиться , вы уже есть в базе!")

