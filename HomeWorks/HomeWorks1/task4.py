# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского 
# ввода три строки: первое число, второе число и операцию, после чего применяет операцию 
# к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def calc (input_data):
    if input_data[2] == '+':
        return input_data[0] + input_data[1]
    if input_data[2] == '-':
        return input_data[0] - input_data[1]
    if input_data[2] == '/':
        if input_data[1] !=0:
            return input_data[0] / input_data[1]
        else:
            print('ОШИБКА! Деление на 0!')
    if input_data[2] == '*':
        return input_data[0] * input_data[1]
    if input_data[2] == 'mod':
        return input_data[0] % input_data[1]
    if input_data[2] == 'pow':
        return input_data[0] ** input_data[1]
    if input_data[2] == 'div':
        if input_data[1] !=0:
            return input_data[0] // input_data[1]
        else:
            print('ОШИБКА! Деление на 0!')

try:
    print('Калькулятор! Введите 2 числа и операцию!')
    input_num = [0,0,0]
    operation = ['+', '-', '/', '*', 'mod', 'pow', 'div']
    while input_num[2] not in operation:
        input_num[0] = float(input('Введите первое число: '))
        input_num[1] = float(input('Введите второе число: '))
        print('Поддерживаемые операции: +, -, /, *, mod, pow, div, где \nmod — это взятие остатка от деления, \npow — возведение в степень, \ndiv — целочисленное деление.')
        input_num[2] = input('Введите операцию: ')
    print(f'{input_num[0]} {input_num[2]} {input_num[1]} = {calc(input_num)}')
except:
    print('Введите число!')