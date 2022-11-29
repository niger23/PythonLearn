import telebot
from telebot import *
from calc_complex import *
from calc_ration import *
from spy import *

API_TOKEN = "5897355132:AAHquqfoMDAyzj6I5SUaMPlVQBfalzoYP30"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Бот-калькулятор, умеет считать рациональные и комплексные выражения!')
    msg = bot.send_message(message.chat.id, 'для комплексных выражений используй i')
    bot.register_next_step_handler(msg, calc)

def calc (message):
    res = message.text
    if 'i' in res:
        result = test(res)
        log(res, result)
        msg = bot.send_message(message.chat.id, f'{res} = {result}')
    else:
        result = simple_calc(res)
        log(res, result)
        msg = bot.send_message(message.chat.id, f'{res} = {result}')
    msg = bot.send_message(message.chat.id, 'Чтобы посчитать следующиее выражение введи его:')
    bot.register_next_step_handler(msg, calc)

print('сервер запущен')
bot.polling()


