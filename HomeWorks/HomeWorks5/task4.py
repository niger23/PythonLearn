# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re


def load ():
    with open('HomeWorks/HomeWorks5/task4.txt', 'r') as ff:
        poly = ff.read()
    print('Файл с уравнениями успешно загружен')
    return poly

def sum_poly ():
    poly = load()
    print(f'Исходные многочлены: \n{poly}')
    new = re.split('[+\n ]', poly)
    new = list(filter(None, new))

    step = {}
    sum_end = 0
    sum_pre_end = 0
    for i in new:
        if '*x^' in i:
            value = re.findall(r'\d+',i)
            if value[1] in step:
                step[value[1]] = int(value[0]) + int(step[value[1]])
            else:
                step[value[1]] = value[0]
        elif 'x' in i:
            value = re.findall(r'\d+',i)
            sum_pre_end += int(value[0])
        elif i.isdigit():
            sum_end += int(i)

    result = ''
    for i, j in step.items():

        result += str(j) + '*x^' + str(i) + ' + '
    result+= str(sum_pre_end) + 'x + ' + str(sum_end)
    return result

result = sum_poly()
print(f'Сумма многочленов: \n{result}')