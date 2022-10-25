# 36. Дан список чисел. Создайте список, в который 
# попадают числа, описывающие максимальную возрастающую 
# последовательность. Порядок элементов менять нельзя. 
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] =>  [1, 7]
#     [1, 2, 8, 1 2, 3, 4,  1, 7] =>  [1, 4]

def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите число: ')) != '':
        list.append(int(value))
    return list

def find_sequence (list):
    min_value = min(list)
    for i in range(len(list)):
        if min_value in list:
            min_value += 1
        result = [min(list), min_value - 1]
    return result

try:
    print('Найдём исключительные значения вашего списка!')
    new_list = create_list()
    print(f'Исходный список: \n{new_list}')
    result = find_sequence(new_list)
    print(f'Максимальная последовательность: \n{result}')

except ValueError as error:
    print(f'Введите целое число! - {error}')