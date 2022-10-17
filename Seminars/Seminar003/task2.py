# 4. Задайте список из N элементов, заполненных числами
#  из промежутка [-N, N]. Найдите произведение элементов
#   на указанных позициях. Позиции хранятся в файле file.txt
#    в одной строке одно число.

from random import randint

def create_file(n):
    with open('file2.txt', 'w') as data:
        for i in range(3):
            value = str(randint(0,n-1))
            data.write(value)
            data.write('\n')

def create_list (n):
    list = []
    for i in range(n):
        list.append(randint(-n,n))
    return list

def multiply (list):
    data = open('file2.txt', 'r')
    res = 1
    for line in data:
        print(f'Элемент на позиции {line}равен: {list[int(line)]}')
        res *=list[int(line)]
    data.close()
    return res

try:
    num = int(input('Введите целое число: '))
    create_file(num)
    new_list = create_list(num)
    print(new_list)
    print(f'Произведение элементов равно: {multiply(new_list)}')
 
except ValueError as error:
    print(f'Введите целое число! - {error}')