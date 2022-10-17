# Задача 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def create_list():
    list = []
    print('Заполните список целыми числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите целое число: ')) != '':
        list.append(int(value))
    return list

def multiply_first_last(list):
    result = []
    size = len(list)//2
    if len(list)%2 != 0: size +=1
    for i in range(size):
        result.append(list[i]*list[-1-i])
    return result

try:
    print('Давайте найдём произведение пар чисел вашего списка!')
    print('Парой считаем первый и последний элемент, второй и предпоследний и т.д.!')
    new_list = create_list()
    print('Исходный список:')
    print(new_list)
    result = multiply_first_last(new_list)
    print('Получился такой список с произведениями:')
    print(result)

except ValueError as error:
    print(f'Введите целое число! - {error}')