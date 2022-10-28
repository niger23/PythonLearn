# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие 
# максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]



def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значение!')
    while (value := input('Введите число: ')) != '':
        list.append(int(value))
    return list

def find_sequence (list):
    min_value = min(list)
    max_value = max(list)
    result = []
    start = min_value
    for i in range(min_value + 1, max_value + 1):
        if i in list:
            end = i
            if i == max_value and start != i:
                result.append([start,max_value])
        else:
            if (end - start) >= 1:
                result.append([start,end])
            start = i + 1
            end = i + 1
    return result

try:
    print('Найдём максимльную последовательность вашего списка!')
    new_list = create_list()
    print(f'Исходный список: \n{new_list}')
    result = find_sequence(new_list)
    if len(result) == 1:
        print(f'Максимальная последовательность вашего списка: \n {result[0]}')
    else:
        max = result[0]
        for i in range(1,len(result)):
            if (result[i][1] - result [i][0]) > (max[1] - max[0]):
                max = result[i]
        print(f'Максимальная последовательность вашего списка: \n {max}')

except ValueError as error:
    print(f'Введите целое число! - {error}')