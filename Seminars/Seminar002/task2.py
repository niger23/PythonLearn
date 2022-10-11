# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в 
# этой четверти (x и y).

# def how_points (num):
#     if num == 1:
#         print(' x > 0; y > 0')
#     elif num == 2:
#         print(' x < 0; y > 0')
#     elif num == 3:
#         print(' x < 0; y < 0')
#     elif num == 4:
#         print(' x > 0; y < 0')
#     else:
#         print('Введите целое число от 1 до 4')

# try:
#     num = int(input('Введите число от 1 до 4: '))
#     how_points(num)
# except:
#     print('Введите целое число')

num = int(input("Введите номер четверти: "))

match num:
    case 1:
        print(" x > 0; y > 0")
    case 2:
        print(" x < 0; y > 0")
    case 3:
        print(" x < 0; y < 0")
    case 4:
        print(" x > 0; y < 0")
    case _:
        print("Что то не так")

    