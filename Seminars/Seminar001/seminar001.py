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

def create_list():
    array = []
    for i in range(1,6):
        value = int(input("Введите число: "))
        array.append(value)
    return array
def find_max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i]>max:
            max = array[i]
    return max

res = create_list()
print(res)
max = find_max(res)
print(f"Максимальное значение в списке равно {max}")


