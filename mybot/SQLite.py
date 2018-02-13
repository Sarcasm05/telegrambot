# -*- coding: utf-8 -*-
import sqlite3

class liter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM users').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE id = ?', (rownum,)).fetchall()[0]

    def select_single_task(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM tasks WHERE number = ?', (rownum,)).fetchall()[0]        

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

    def accept_status_task(self, id, task_id):
        """Пользователь теперь выполняет задание"""
        with self.connection:
            self.cursor.execute('UPDATE users SET task_status="YES" WHERE id= ?',(id, ))
            self.cursor.execute('UPDATE users SET task_id=? WHERE id= ?',(task_id,id, ))

    def cancel_status_task(self, id):
        """Отменяем выполнение задания"""
        with self.connection:
            self.cursor.execute('UPDATE users SET task_status="EMPTY" WHERE id= ?',(id, ))
            self.cursor.execute('UPDATE users SET task_id=0 WHERE id= ?',(id, ))

    def add_money(self, id, coin):
        #Добавляем монеты
        with self.connection:
            self.cursor.execute('UPDATE users SET  money= money + ? WHERE id= ?',(coin,id, ))        

