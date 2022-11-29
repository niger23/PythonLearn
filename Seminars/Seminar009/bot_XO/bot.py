import telebot
from telebot import *
import random
from random import randint
import numpy as np

API_TOKEN = "5897355132:AAHquqfoMDAyzj6I5SUaMPlVQBfalzoYP30"

bot = telebot.TeleBot(API_TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('1 1', '1 2', '1 3')
keyboard.row('2 1', '2 2', '2 3')
keyboard.row('3 1', '3 2', '3 3')

count = 0
game_field = []

@bot.message_handler(commands=['start'])
def start_message(message):
    global count
    global game_field
    count = 0
    game_field = []
    for i in range(3):
        game_field_1 = []
        for j in range(3):
            game_field_1.append('_')
        game_field.append(game_field_1)
    global player_turn
    bot.send_message(message.chat.id,'Сыграем в крестики-нолики!')
    player_turn = randint(0,1)

    if player_turn:
        bot.send_message(message.chat.id,'Вы делаете первый ход')
        bot.send_message(message.chat.id,f'{game_field[0]}\n{game_field[1]}\n{game_field[2]}')
        msg = bot.send_message(message.chat.id, 'Введите номер строки и столбца через пробел: ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, body_game)
    else: 
        bot.send_message(message.chat.id,'Компьютер делает первый ход')
        body_game(message)

def body_game(message):
    global player_turn
    global count
    global game_field
    
    if player_turn:
        res = message.text.split()
        x = int(res[0])-1
        y = int(res[1])-1
        if wrong_value(x) or wrong_value(y):
            bot.send_message(message.chat.id,'Ячейка за пределами поля')

        if game_field[x][y] == '_':
            game_field[x][y] = 'x'
            bot.send_message(message.chat.id,f'{game_field[0]}\n{game_field[1]}\n{game_field[2]}')
            count+=1
            player_turn = not player_turn
        else:
            bot.send_message(message.chat.id,f'Клетка [{x+1}, {y+1}] уже занята.')
    
    else:
        not_free = False
        bot.send_message(message.chat.id,'Ход компьютера:')
        while not_free == False:
            x = random.randrange(0,3)
            y = random.randrange(0,3)
            if game_field[x][y] == '_':
                not_free = True
                game_field[x][y] = 'o'
                bot.send_message(message.chat.id,f'{game_field[0]}\n{game_field[1]}\n{game_field[2]}')
                count+=1
                player_turn = not player_turn
    
    if check_win(game_field) == 0 and count > 8:
        bot.send_message(message.chat.id,'Ничья!')
        welcome_help(message)
    elif check_win(game_field) == 1:
        bot.send_message(message.chat.id,'Вы выиграли!')
        welcome_help(message)
    elif check_win(game_field) == 2:
        bot.send_message(message.chat.id,'Бот выиграл!')
        welcome_help(message)
    else:
        if player_turn:
            msg = bot.send_message(message.chat.id, 'Введите номер строки и столбца через пробел: ', reply_markup=keyboard)
            bot.register_next_step_handler(msg, body_game)
        else: 
            body_game(message)
   
def check_win(game_field):
    count_p = 0
    count_b = 0
    if game_field[0][2] == 'x' and game_field[1][1] == 'x' and game_field[2][0] == 'x':
        count_p = 3
    if game_field[0][2] == 'o' and game_field[1][1] == 'o' and game_field[2][0] == 'o':
        count_b = 3
    for i in range(3):
        if game_field[i][i] == 'x':
            count_p += 1
        if game_field[i][i] == 'o':
            count_b += 1
        col = np.array(game_field)         
        col = list(col[:, i])
        if game_field[i].count('x') == 3 or col.count('x') == 3 or count_p == 3:
            return 1
            break
        elif game_field[i].count('o') == 3 or col.count('o') == 3 or count_b ==3:
            return 2
            break
    return 0


def wrong_value(n):
    if n not in range (3):
        return True

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, '/start - чтобы начать заново')


print('сервер запущен')
bot.polling()