# задача 3. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def create_list(k):
    form = ''
    for i in range(k, 0, -1):
        if i > 1:
            form = form + str(randint(0,101)) + '*x^'+ str(i) + ' + '
        elif i == 1:
            form = form + str(randint(0,101)) + '*x' + ' + ' + str(randint(0,101)) + ' = 0'
    
    return form

def save_in_file (list):
    with open('HomeWorks/HomeWorks4/task3.txt', 'w') as ff:
        ff.write(list)
    print('Многочлен сохранён в файле!')

try:
    print('Создадим и сохраним многочлен степени k!')
    num = int(input('Введите k, степень многочлена: '))
    if num >= 1:
        list = create_list(num)
        print(f'Получился следующий многочлен: \n{list}')
        save_in_file(list)
    else:
        print('Число k должно быть целым положительным!')

except ValueError as error:
    print(f'Введите целое положительное число! - {error}')