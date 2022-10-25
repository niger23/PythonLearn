# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит 
# через строку пользователь. например, 6*x^2+5*x+6=0 . Само собой, уравнение
# может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.

import re
import math

def solving_equation (str):
    digits = re.split('[+-]', str)
    new = []
    for i in digits:
        new.append(re.sub('[^0-9]', '', i))
    for i in range(len(digits)):
        if ('x^2' in digits[i]) or ('x**2' in digits[i]):
            a = int(new[i][0:-1])
        elif 'x' in digits[i]:
            b = int(new[i])
        elif '=' in digits[i]:
            c = int(new[i][0:-1])
    elem = []
    for i in range(len(str)):
        if '-' == str[i] or '+' == str[i]:
            elem.append(str[i])
            
    if elem[0] == '-':
        b=-b
    if elem[1] == '-':
        c=-c
    print(f'Кооэффициенты:\na = {a},\nb = {b},\nc = {c}.')
    discr = b ** 2 - 4 * a * c
    print(f"Дискриминант D = {round(discr)}")

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f"x1 = {round(x1)} \nx2 = {round(x2)}")
    elif discr == 0:
        x = -b / (2 * a)
        print(f"x = {round(x)}")
    else:
        print("Корней нет")


print('Найдите корни квадратного уравнения!')
print('Уравнение введите через строку, например: 6*x^2+5*x+6=0')
str = input('Введите уравнение: ')
# str = '236x**2-595x-66=0'
# str = '6*x^2+5*x+6=0'
solving_equation(str)