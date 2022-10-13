# Задача 2. Напишите программу, которая принимает на вход число 
# N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (num):
    fac_list = []
    fac = 1
    for i in range(1, num + 1):
        fac *= i
        fac_list.append(fac)
    return fac_list

try:
    print('Найдём значения факториала от 1 до вашего числа!')
    num = int(input('Введите целое число: '))
    print(factorial(num))
except:
    print('Введите целое число!')