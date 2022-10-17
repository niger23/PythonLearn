# 3. Задайте список из n чисел последовательности (1+1/N)**N
#  и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from distutils.log import error


def sum_list (list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def create_list (n):
    list = []
    for i in range(1,n+1):
        list.append(round((1+1/i)**i, 3))
    return list

try:
    num = int(input('Введите целое число: '))
    new_list = create_list(num)
    print(new_list)
    print(f'Сумма элементов последовательности: {round(sum_list(new_list),3)}')
except ValueError as error:
    print(f'Введите целое число! - {error}')