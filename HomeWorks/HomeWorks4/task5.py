# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем 
# на основе приложенного буткемпа. Тема чат-бота любая. Просьба - постараться 
# не использовать простой одномерный список или простой одномерный словарь.

from random import *
import random
import json

books = {}

while True:
    command = input('Введите команду: ')
    if command == '/start':
        print('Бот-библиотека по Python начал свою работу')
    elif command == '/stop':
        print('Бот остановил свою работу и сохранил последние изменения. Заходи ещё!')
        with open('HomeWorks/HomeWorks4/books.json', 'w', encoding="utf-8") as fh:
            fh.write(json.dumps(books,ensure_ascii=False))
        break
    elif command == '/all':
        print('Вот текущий список книг:')
        for key, value in books.items():
            print("{0}: {1}".format(key,value))
    elif command == '/add':
        f = input('Введите название книги: ')
        f2 = input('Введите автора книги: ')
        books[f] = f2
        print(f'Книга {f} - {f2} добавлена в коллекцию!')
    elif command == '/help':
        print('Здесь список всех комманд')
    elif command == '/del':
        d = input('Введите название книги для удаления: ')
        try:
            del books[d]
            print(f'Книга {d} успешно удалёна!')
        except:
            print(f'Книга {d} не найдена в коллекции!')
    elif command == '/random':
        random_book = {}
        key, value = random.choice(list(books.items()))
        random_book[key] = value
        for key, value in random_book.items():
            print(f'Предлагаем почитать: {key} - {value}')
    elif command == '/save':
        with open('HomeWorks/HomeWorks4/books.json', 'w', encoding="utf-8") as fh:
            fh.write(json.dumps(books,ensure_ascii=False))
        print('Наша библиотека была успешно сохранена в файле books.json')
    elif command == '/load':
        with open('HomeWorks/HomeWorks4/books.json', 'r', encoding="utf-8") as fh:
            books = json.load(fh)
        print('Библиотека была успешно загружена!')
    else:
        print('Неопознанная команда. Просьба изучить материал через /help')