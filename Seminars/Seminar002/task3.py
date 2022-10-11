# 5. Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.   
#     *Пример:*   
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def length (point1, point2, size):
    for i in range(size):
        result = sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return result

try:

    point1 = [0]*2
    point2 = []
    point1[0] = float(input('Введите значение Х 1 точки: '))
    point1[1] = float(input('Введите значение Y 1 точки: '))
    point2.append(float(input('Введите значение Х 2 точки: ')))
    point2.append(float(input('Введите значение Y 2 точки: ')))
    res = length(point1, point2)
    print(f'Расстояние между точками {point1} и {point2} равно: {round(res, 3)}')
except:
    print('Введите число')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# import math
# try:
#     coordA = []
#     for i in range(2):
#         coordA.append(int(input("введите координату точки А: ")))
#     coordB = []
#     for i in range(2):
#         coordB.append(int(input('введите координату точки В: ')))
#     print(coordA, coordB)
    
#     distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
#     print(round(distan, 3))
# except:
#     print('Введите числа')
