import sqlite3 as sq


def add_book(book: list):
      """
    Функция на вход получает список, состоящий из названия, автора, и года выпуска книги
    После получения добавляет в базу данных новую книгу, содержащую введёные данные
      """
      with sq.connect('libary.db') as con:
            cur = con.cursor()      
            cur.execute('INSERT INTO Libary (name, authtor, year) VALUES(?,?,?)',(book[0], book[1], book[2]))

      print(f'Книга {book[0]} от автора {book[1]} {book[2]} года выпуска добавленна')

def check_book():
      """
    Функция выводит все книги имеющиеся в базе данных
      """
      with sq.connect('libary.db') as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM Libary')
            print(*cur.fetchall(), sep="\n")

def change_status(book):
      """
    Функция на вход получает список из двух элементов, один из которых id книги, а другой новый статус,
    После получения функция изменяет статус у книги с ведённым id
      """
      
      
      book_id = book[0]
      book_status = book[1]
      with sq.connect('libary.db') as con:
            cur = con.cursor()
            cur.execute(f'UPDATE Libary SET status = "{book_status}"  WHERE id = {book_id}')

def delete_book(book_id):
      """
    Функция на вход получает id книги, после чего удаляет её из базы данных
      """
      
      with sq.connect('libary.db') as con:
            cur = con.cursor()
            cur.execute(f'DELETE FROM Libary WHERE id = {book_id} ')


with sq.connect('libary.db') as con: # При первом запуске создаёт sql таблицу
      cur = con.cursor()      
      cur.execute(""" CREATE TABLE IF NOT EXISTS Libary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            authtor TEXT,
            year INT,
            status DEFAULT 'В наличии'
            )""")
               
menu_print = True


menu = '''
[1] Добавить книгу в библиотеку
[2] Просмотреть спикок книг
[3] Удаление книги
[4] Измнение статуса книги
[menu] Вернуться в списко команд
'''      
print(menu)

while True:
      callback = input('>>> ')
      if callback == '1':
            print('Введите книгу через пробел по следующему образцу\nНазвание Автор Год выпуска')
            add_book(input('>').split())
      if callback == '2':
            check_book()
      if callback == '3':
            print('Введите id книги, которую нужно удалить')
            delete_book(input('>'))
      if callback == '4':
            print('Введите статус книги которой нужно изменить через пробел \nПример: 1 Выдана')
            change_status(input('>').split())
      
