# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

from random import randint

def steps_bot(hard_mode, sweets):
    if sweets > 29:
        if hard_mode == 1:
            if sweets % 29 == 0:
                step_bot = 28
            else:
                step_bot = sweets % 29
        else:
            step_bot = randint(1,28)
    else:
        if hard_mode == 1:
            step_bot = sweets
        else:
            step_bot = randint(1,sweets)
    return step_bot


def game_sweets ():
    print('Давай поиграем в игру!')
    print('На столе лежит 2021 конфета.\nЗа один ход можно забрать не более чем 28 конфет.')
    print('Все конфеты оппонента достаются сделавшему последний ход.')
    hard_mode = int(input('Введите 1 если хотите сыграть в HARD режим, 0 если в простой: '))
    if not (hard_mode == 1 or hard_mode == 0):
        print('Требуется ввести только 0 или 1')
        exit()
    first_step = randint(0,1)
    if first_step == 0: print('Жеребьёвкой решено, что первым ходит "бот"!')
    else: print('Жеребьёвкой решено, что первым ходишь ты!')
    sweets = 2021
    if first_step == 0:
        step_bot = steps_bot(hard_mode, sweets)
        print(f'Бот забирает {step_bot}')
        sweets -= step_bot

    while sweets > 0:
        print(f'Конфет на столе: {sweets}')
        while True:
            try:
                print('Конфет можно взять от 1 до 28 и не более количества на столе!')
                step = int(input('Сколько конфет забираем: '))
                if step > 28 or step < 1 or step > sweets:
                    continue
                else:
                    sweets -= step
                    print(f'Конфет на столе осталось: {sweets}')
                    break
            except ValueError as error:
                print(f'Введите целое положительное число!')
                continue

        if sweets == 0:
            print('Ты выиграл!')
        elif sweets > 0:
            step_bot = steps_bot(hard_mode, sweets)
            print(f'Бот забирает {step_bot}')
            sweets -= step_bot
            if sweets == 0:
                print('Ты проиграл!')

game_sweets()
