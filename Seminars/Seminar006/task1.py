import random
from random import randint
import numpy as np

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
            print('Вы победили!')
            return 1
            break
        elif game_field[i].count('o') == 3 or col.count('o') == 3 or count_b ==3:
            print('Компьютер победил!')
            return 1
            break
    return 0


def wrong_value(n):
    if n not in range (3):
        print(f'Значение {n} за пределами поля')
        return True

def create_field():
    game_field = []
    for i in range(3):
        game_field_1 = []
        for j in range(3):
            game_field_1.append('_')
        game_field.append(game_field_1)
    return game_field

def print_field(game_field):
    for i in range(3):
        print(' '.join(game_field[i]))


def main():
    print('Сыграем в крестики-нолики!')
    game_field = create_field()

    player_turn = randint(0,1)
    print('Вы делаете первый ход' if player_turn else 'Компьютер делает первый ход')

    for _ in range(9):
        
        print_field(game_field)
        if player_turn:
            x, y = map(int, input('Введите номер строки и столбца через пробел: ').split())
            x, y = x-1, y-1
            if wrong_value(x) or wrong_value(y):
                continue

            if game_field[x][y] == '_':
                game_field[x][y] = 'x'
            else:
                print(f'Клетка [{x+1}, {y+1}] уже занята. Ход переходит компьютеру.')
        
        else:
            not_free = False
            print('Ход компьютера:')
            while not_free == False:
                x = random.randrange(0,3)
                y = random.randrange(0,3)
                if game_field[x][y] == '_':
                    not_free = True
                    game_field[x][y] = 'o'

        player_turn = not player_turn
        
        if check_win(game_field) == 1:
            break
    print_field(game_field)
    if check_win(game_field) == 0:
        print('Ничья!')
main()
