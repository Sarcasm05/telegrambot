import sqlite3
import telebot
import config
from SQLite import liter
from keyboard_class import Keyboard
bot = telebot.TeleBot(config.token)


def status_task(message):       #Проверить статус выполнения задания пользователем
    bd = liter(config.database_name)
    c = bd.select_single(message.from_user.id)
    if c[2] == 'NO':
        bd.close()
        count = 'NO'
        return count
    elif c[2] == 'EMPTY' :
        bd.close()
        count = 'EMPTY'
        return count 
    else:
        bd.close()
        count = 'YES'
        return count

def show_my_task(message):       #Показать задание пользователя
    bd_user = liter(config.database_name) # открываем бд пользователей
    row = bd_user.select_single(message.from_user.id)
    task_id = row[1] #id задания
    bd_user.close()

    bd_task = liter(config.tasks_base)# открываем бд заданий
    row_task = bd_task.select_single_task(task_id) 
    task = row_task[2] #Задание
    bot.send_message(message.from_user.id, task)
    bd_task.close()

def accept_task(message,task_number):       #Принять задание 
    bd_task = liter(config.tasks_base)# открываем бд заданий
    row_task = bd_task.select_single_task(task_number) 
    task = row_task[2] #Задание
    task_id = row_task[0]
    bot.send_message(message.from_user.id, "Вы приняли задание : ")
    bot.send_message(message.from_user.id, task)
    bd_task.close()

    bd_user = liter(config.database_name)
    bd_user.accept_status_task(message.from_user.id,task_id)
    bd_user.close()

def cancel_task(message):       #Отмена задания
    bd_user = liter(config.database_name)
    bd_user.cancel_status_task(message.from_user.id)
    bot.send_message(message.from_user.id, "Вы  отменили задание.")
    bd_user.close()

def done_task(message):         #Задание выполнено
    bd_user = liter(config.database_name)
    row = bd_user.select_single(message.from_user.id)
    task_id = row[1]
    bd_task = liter(config.tasks_base)
    row_task = bd_task.select_single_task(task_id)
    task_cost = row_task[3]
    bd_user.cancel_status_task(message.from_user.id)
    bd_user.add_money(message.from_user.id, task_cost)
    bot.send_message(message.from_user.id, "Вы  выполнили задание, заработав {0} монет".format(task_cost))
    bd_user.close()
    bd_task.close()


def get_task(message):    
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

