# 1. Напишите программу, которая принимает на вход два 
# числа и проверяет, является ли одно число квадратом другого.

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# if num1 == num2*num2 or num2 == num1*num1:
#     print("Одно число является квадратом другого числа")
# else:
#     print("Одно число не является квадратом другого числа")

# try:
#     number1 = int(input('Введите первое число: '))
#     number2 = int(input('Введите второе число: '))
#     if number1 ** 2 == number2:
#         print(f'{number2} является квадратом числа {number1}')
#     elif number2 ** 2 == number1:
#         print(f'{number1} является квадратом числа {number2}')
#     else:
#         print('Ни одно из числе не является квадратом другого')
# except:
#     print('Введите целое число')


# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.

# def create_list():
#     array = []
#     for i in range(5):
#         value = int(input("Введите число: "))
#         array.append(value)
#     return array
# def find_max(array):
#     max = array[0]
#     for i in range(len(array)):
#         if array[i]>max:
#             max = array[i]
#     return max

# res = create_list()
# print(res)
# max = find_max(res)
# print(f"Максимальное значение в списке равно {max}")


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# def digits (num):
#     for i in range(-num, num + 1):
#         print(i, end=' ')   
# try:
#     current = int(input("Введите число: "))
#     digits(current)

# except:
#     print('Введите целое число')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# def find_first_number(number):
#     res = number
#     number *= 10
#     res = int(number % 10)
#     return res

# try:
#     num = float(input("Введите число: "))
#     print(find_first_number(num))
# except:
#     print('Введите целое число')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def multiple(num):
    if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0:
        print("Число удовлетворяет данным условиям")
    else:
        print("Число не удовлетворяет данным условиям")
try:
    num = int(input("Введите число: "))
    multiple(num)
except:
    print('Введите целое число')
