import telebot


class Keyboard:
    def __init__(self, bot):
        self.bot = bot



    def show_money(self,message):
        money_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        money_markup.row('Обновить балланс')
        money_markup.row('Главное меню')
        self.bot.send_message(message.from_user.id,'Выберите пункт меню:',
                             reply_markup=money_markup)


    def my_task(self,message):
        task_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        task_markup.row("Выполнил задание")
        task_markup.row("Отменить задание")
        task_markup.row('Главное меню')
        self.bot.send_message(message.from_user.id,'Выберите пункт меню:',
                             reply_markup=task_markup)

    def show_social(self,message):
        social_markup = telebot.types.InlineKeyboardMarkup()
        btn_my_site = telebot.types.InlineKeyboardButton(text='Twitter',
                                    url='https://twitter.com/W0rldBlockchain')
        social_markup.add(btn_my_site)
        btn_my_site = telebot.types.InlineKeyboardButton(text='Youtube',
                url='https://www.youtube.com/channel/UC4pqIogmWRtSD4l8Ikc5Itg')
        social_markup.add(btn_my_site)
        self.bot.send_message(message.from_user.id, "Наши соцсети:",
                            reply_markup=social_markup)

    def show_tasks(self, message):
        date_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        date_markup.row("Принять задание")
        date_markup.row("Следующее задание")
        date_markup.row('Главное меню')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:',
                             reply_markup=date_markup)

    def main_menu_task(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Мое задание")
        user_markup.row("Показать соц сети")
        user_markup.row("Проверить балланс")
        #user_markup.row('Обновления', 'Обратная связь')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:',
                             reply_markup=user_markup)
    def main_menu(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Начать работу")
        user_markup.row("Показать соц сети")
        user_markup.row("Проверить балланс")
        #user_markup.row('Обновления', 'Обратная связь')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:',
                             reply_markup=user_markup)


