# задача 2 . Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите число: ')) != '':
        list.append(int(value))
    return list

def find_unique(numbers):
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique

try:
    print('Найдём исключительные значения вашего списка!')
    new_list = create_list()
    print(f'Исходный список: \n{new_list}')
    result = find_unique(new_list)
    print(f'Список уникальных элементов: \n{result}')

except ValueError as error:
    print(f'Введите целое число! - {error}')