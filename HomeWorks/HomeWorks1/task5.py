# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается
#  с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

from random import randint

def create_array(n,m):
    array = [[randint(1,100) for j in range(m)] for i in range(n)]
    return array

def show_array(array):
    for i in range(len(array)):
        print(array[i][:])

def sort_array(array, n, m):
    result = [[[0] for j in range(n)] for i in range(m)]
    max = 0
    for x in range(0,n):
        for y in range(0,m):
            min = array[0][0]
            while min == 0:
                min = max
            min_i = [0, 0]
            for i in range(0,n):
                for j in range(0,m):
                    if min > array[i][j] and array[i][j] !=0:
                        min = array[i][j]
                        min_i = [i, j]
                    if max < array[i][j]:
                        max = array[i][j]
            result[x][y] = min
            array[min_i[0]][min_i[1]] = 0
    return result

try:
    n = int(input('Введите количество строк массива: '))
    m = int(input('Введите количество столбцов массива: '))

    new_array = create_array(n,m)
    show_array(new_array)
    result_array = sort_array(new_array, n, m)
    print('--------------------')
    print('Отсортированный массив')
    print('--------------------')
    show_array(result_array)
except:
        print('Введите целое число!')