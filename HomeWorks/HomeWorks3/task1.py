# Задача 1 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите число: ')) != '':
        list.append(int(value))
    return list

def sum_no_even_index(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum+= list[i]
    return sum

try:
    print('Давайте найдём сумму нечётных элементов вашего списка!')
    new_list = create_list()
    print('Получился такой список:')
    print(new_list)
    result = sum_no_even_index(new_list)
    print(f'Сумма элементов стоящих на нечётных позициях равна: {result}')

except ValueError as error:
    print(f'Введите целое число! - {error}')
