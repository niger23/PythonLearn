# задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def factorization (num):
    result = []
    for i in range(2, int(num**0.5+1)):
        while not num % i:
            result.append(i)
            num /= i
    if num > 1:
        result.append(int(num))
    return result

try:
    print('Составим список простых множителей вашего числа!')
    num = int(input('Введите число: '))
    result = factorization(num)
    print(f'Множетели: {result}')

except ValueError as error:
    print(f'Введите целое число! - {error}')