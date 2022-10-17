# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n 
# (размерность вводим с клавиатуры) , причем чтоб количество элементов 
# было четное. Вывести на экран красивенько таблицей. Перемешать 
# случайным образом элементы массива, причем чтобы каждый 
# гарантированно переместился на другое место и выполнить это за 
# m*n / 2 итераций. То есть если массив три на четыре, то надо 
# выполнить не более 6 итераций. И далее в конце опять вывести на 
# экран как таблицу.

from random import randint

def create_array(n,m):
    array = [[randint(1,100) for j in range(m)] for i in range(n)]
    return array

def show_array(array):
    for i in range(len(array)):
        print(array[i][:])

def list_sort(n,m):
    list_sort = []
    for i in range(n//2,n):
        for j in range(m):
            list_sort.append([i,j])
    return list_sort

def resort_array (array, list_sort, n, m):
    global new_list_sort
    for i in range(n//2):
        for j in range(m):
            value = randint(0, len(list_sort)-1)
            array[i][j], array[list_sort[value][0]][list_sort[value][1]] = array[list_sort[value][0]][list_sort[value][1]], array[i][j]
            new_list_sort.remove(list_sort[value])
    return array


try:
    print('Количество строк должно быть чётным!')
    n = int(input('Введите количество строк массива: '))
    m = int(input('Введите количество столбцов массива: '))

    if n%2 == 0:
        new_array = create_array(n,m)
        show_array(new_array)

        print('--------------------')
        print('Перемешанный массив')
        print('--------------------')

        new_list_sort = list_sort(n,m)
        result_array = resort_array(new_array, new_list_sort,n,m)
        show_array(result_array)
    else:
        print('Количество строк должно быть чётным!')

except ValueError as error:
    print(f'Введите целое число! - {error}')
