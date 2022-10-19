# 3. Задайте два числа. Напишите программу, которая 
# найдёт НОК (наименьшее общее кратное) этих двух чисел.

# НОД

# def check_nok (num1, num2):
#     if num1 > num2:
#         num1,num2 = num2,num1
#     for i in range(2,num1+1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             print(f'НОК = {i}')
#             break

# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
# check_nok(num1,num2)

# НОК

def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i


def main():
    try:
        a = int(input('Input number A: '))
        b = int(input('Input number B: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print(f'LCM({a}, {b}) = {lcm(a, b)}')


if __name__ == '__main__':
    main()
