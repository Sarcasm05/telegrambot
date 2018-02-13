# -*- coding: utf-8 -*-
#By Brdsky
import random
import sqlite3
import telebot
import config
from keyboard_class import Keyboard
bot = telebot.TeleBot(config.token)
import functions
keyboard = Keyboard(bot)


@bot.message_handler(commands=['start'])
def handle_text(message):
    if functions.autorisation(message) == False:
    	functions.add_user(message)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Начать работу")
    user_markup.row("Показать соц сети")
    user_markup.row("Проверить балланс")
    #user_markup.row('Обновления', 'Обратная связь')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', 
    				reply_markup=user_markup)

@bot.message_handler(func=lambda mess: "Главное меню" == mess.text, 
					content_types=['text'])
def handle_text(message):
	if functions.status_task(message) == "YES":
		keyboard.main_menu_task(message)
	else:
		keyboard.main_menu(message)

@bot.message_handler(func = lambda mess: "Начать работу" == mess.text, 
					content_types=['text'])
def handle_text(message):
	functions.accept_task(message,random.randint(1,5))
	keyboard.my_task(message)

@bot.message_handler(func = lambda mess: "Показать соц сети" == mess.text,
					content_types=['text'])
def handle_text(message):
	keyboard.show_social(message)

@bot.message_handler(func = lambda mess: "Принять задание" == mess.text,
					content_types=['text'])
def handle_text(message):
	if functions.status_task(message) == "EMPTY":
		functions.accept_task(message)
		#functions.accept_task(message) принять задание , надо реализовать
		keyboard.my_task(message)

@bot.message_handler(func = lambda mess: "Мое задание" == mess.text,
					content_types=['text'])
def handle_text(message):
	if functions.status_task(message) == "YES":
		functions.show_my_task(message)
		keyboard.my_task(message)

@bot.message_handler(func = lambda mess: "Отменить задание" == mess.text,
					content_types=['text'])
def handle_text(message):
	if functions.status_task(message) == "YES":
		functions.cancel_task(message)
		keyboard.main_menu(message)

@bot.message_handler(func = lambda mess: "Выполнил задание" == mess.text,
					content_types=['text'])
def handle_text(message):
	if functions.status_task(message) == "YES":
		functions.done_task(message)
		keyboard.main_menu(message)

@bot.message_handler(func = lambda mess:
					"Проверить балланс" == mess.text or "Обновить балланс" == mess.text,
 					content_types=['text'])
def handle_text(message):
	functions.get_ballance(message)
	#keyboard.show_money(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)