# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def create_list():
    list = []
    print('Заполните список любыми числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите число: ')) != '':
        list.append(float(value))
    return list

def diff_min_max(list):
    min = max = list[0] - int(list[0])
    for i in range(len(list)):
        value = list[i] - int(list[i])
        if value < min: min = value
        elif value > max: max = value
    result = max - min
    return result

try:
    print('Найдём разницу между максимальным и минимальным значением дробной части элементов!')
    new_list = create_list()
    print('Получился список:')
    print(new_list)
    result = round(diff_min_max(new_list),5)
    print(f'Разница между максимальным и минимальным значением дробной части равна: {result}')

except ValueError as error:
    print(f'Введите число! - {error}')