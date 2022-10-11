# 1. Напишите программу, которая принимает на вход число 
# N и выдаёт последовательность из N членов.
# *Пример:*   
#     - Для N = 5: 1, -3, 9, -27, 81

def print_value(num):
    for j in range(num):
        print((-3)**j, end = " ")


try:
    num = int(input("Введите число: "))
    print_value(num)
except:
    print('Введите число')