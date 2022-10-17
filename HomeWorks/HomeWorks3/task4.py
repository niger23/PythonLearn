# Задача 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. Нельзя использовать готовые функции.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_bynary(num):
    res = ''
    for i in range(int(num**0.5)+1):
        if num > 0:
            res = str(num%2) + res
            num = num // 2
    return res
try:
    print('Переведём число из десятичного в двоичный код!')
    num = int(input('Введите целое число: '))
    result = convert_bynary(num)
    print(f'Число {num} в двоичной системе равно: {result}')

except ValueError as error:
    print(f'Введите целое число! - {error}')
    