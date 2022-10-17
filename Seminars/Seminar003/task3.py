# 20. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

def create_list():
    list = []
    value = 0
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while value != '':
        value = input('Введите значение: ')
        list.append(value)
    list.pop()
    return list



try:
    new_list = create_list()
    print(new_list)
    num = int(input('Введите число, которое будем искать: '))
    if str(num) in new_list:
        print(f'Число {num} найдено в этом списке!')
    else:
        print(f'Число {num} не найдено в этом списке!')
except ValueError as error:
    print(f'Введите целое число! - {error}')


