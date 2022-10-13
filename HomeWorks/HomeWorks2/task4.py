# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает 
# на вход N, и координаты двух точек и находит расстояние между 
# ними в N-мерном пространстве.

def find_length (points):
    sum = 0
    for i in range(len(points[0])):
        sum += (points[0][i] - points[1][i])**2
    return sum**0.5

def create_points (n):
    points = []
    for i in range(2):
        points1 =[]
        for j in range(n):
            points1.append(float(input(f'Введите {j+1} координату, {i+1} точки: ')))
        points.append(points1)
    return points

try:
    print('Найдём расстояние между 2-мя точками в N-мерном пространстве!')
    n = int(input('Введите N, сколько мерное пространство: '))
    if n < 1:
        print('Введите целое положительное число!')
    else:
        points = create_points(n)
        find_length(points)
        print(f'Расстояние между точками: {points[0]} и {points[1]} равна: {round(find_length(points),5)}')
except:
    print('Введите целое число')