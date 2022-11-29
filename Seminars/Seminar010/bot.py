import telebot
from telebot import *
from bd import * 

API_TOKEN = "5897355132:AAHquqfoMDAyzj6I5SUaMPlVQBfalzoYP30"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    global data
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поиск")
    btn2 = types.KeyboardButton("Показать всё")
    btn3 = types.KeyboardButton("Добавить")
    btn4 = types.KeyboardButton("Удалить")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    data = load_table()
    bot.send_message(message.chat.id, f"БД успешно загружена!")

    bot.send_message(message.chat.id, text="Привет, {0.first_name}!\nЯ бот для работы с базой данных.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def commands(message):
    global data
    if(message.text == "Поиск"):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("По фирме")
        btn2 = types.KeyboardButton("По модели")
        btn3 = types.KeyboardButton("По разрешению")
        btn4 = types.KeyboardButton("По размеру")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup2.add(btn1, btn2, btn3, btn4, back)
        msg = bot.send_message(message.chat.id, f"Выбери как будем искать:", reply_markup=markup2)
        bot.register_next_step_handler(msg, choise_find)
    elif(message.text == "Показать всё"):
        for row in data:
            bot.send_message(message.chat.id, f"{row}")
    elif(message.text == "Добавить"):
        msg = bot.send_message(message.chat.id, 'Чтобы добавить новую запись:\nвведите данные через пробел\nФирма Модель Разрешение Размер Цена')
        bot.register_next_step_handler(msg, add_a)
    elif(message.text == "Удалить"):
        msg = bot.send_message(message.chat.id, 'Чтобы удалить запись:\nвведите ID элемента, который нужно удалить')
        bot.register_next_step_handler(msg, del_a)
    else:
        bot.send_message(message.chat.id, f"{message.text} команды не существует")
        start_message(message)

@bot.message_handler(content_types=['text'])
def choise_find(message):
    global fin_d
    fin_d = ['','','','']
    if(message.text == "По фирме"):
        fin_d[0] = 1
        msg = bot.send_message(message.chat.id, 'Какую фирму ищем?')
        bot.register_next_step_handler(msg, find)
    elif(message.text == "По модели"):
        fin_d[1] = 1
        msg = bot.send_message(message.chat.id, 'Какую модель ищем?')
        bot.register_next_step_handler(msg, find)        
    elif(message.text == "По разрешению"):
        fin_d[2] = 1
        msg = bot.send_message(message.chat.id, 'Какое разрешение ищем?')
        bot.register_next_step_handler(msg, find)
    elif(message.text == "По размеру"):
        fin_d[3] = 1
        msg = bot.send_message(message.chat.id, 'Какой размер ищем?')
        bot.register_next_step_handler(msg, find)
    elif(message.text == "Вернуться в главное меню"):
        start_message(message)
    else:
        bot.send_message(message.chat.id, f"{message.text} команды не существует")
        start_message(message)
def find(message):
    global fin_d
    for i in range(len(fin_d)):
        if fin_d[i]:
            fin_d[i] = message.text
    data_f = find_table(fin_d[0],fin_d[1],fin_d[2],fin_d[3])
    for row in data_f:
        bot.send_message(message.chat.id, f"{row}")
    start_message(message)

def del_a(message):
    id_del = message.text
    delete_element(id_del)
    bot.send_message(message.chat.id, f"Запись с ID'{message.text}' успешно удалена")
    start_message(message)


def add_a(message):
    res = message.text.split()
    if len(res) == 5:
        added_element(res)
        bot.send_message(message.chat.id, f"Запись '{message.text}' успешно добавлена")
        start_message(message)
    else:
        bot.send_message(message.chat.id, f"Возможно вы ввели больше или меньше элементов, чем нужно было")
        start_message(message)

print('сервер запущен')
bot.polling(none_stop=True)