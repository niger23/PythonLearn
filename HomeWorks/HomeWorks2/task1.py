# Задача 1. Напишите программу, которая принимает на вход 
# вещественное или целое число и показывает сумму его 
# цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(num):

    if num < 0:
        num = -num

    while round(num, 10) != int(num):
        num *= 10

    sum = 0
    while num != 0:
        sum += int(num) % 10
        num = int(num)/10
    return sum

try:
    print('Посчитаем сумму цифр вашего числа!')
    num = float(input('Введите любое число: '))
    print(f'Сумма цифр числа {num} равна: {sum_digits(num)}')
except:
    print('Введите число')