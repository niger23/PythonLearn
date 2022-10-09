# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def what_quarter (coor):
    if coor[0] > 0 and coor[1] > 0:
        return 1
    elif coor[0] < 0 and coor[1] > 0:
        return 2
    elif coor[0] < 0 and coor[1] < 0:
        return 3
    elif coor[0] == 0:
        return 11                
    elif coor[1] == 0:
        return 22
    else:
        return 4
try:
    print('Узнаем в какой четверти находится точка!')
    print('X и Y одновременно не должны быть равны 0!')
    coordinate = [0,0]
    while coordinate[0] == 0 and coordinate[1] == 0:
        coordinate[0] = float(input('Введите координату X: '))
        coordinate[1] = float(input('Введите координату Y: '))
    if what_quarter(coordinate) == 11:
        print(f'Точка с координатами {coordinate}, находится на оси Y!')
    elif what_quarter(coordinate) == 22:
        print(f'Точка с координатами {coordinate}, находится на оси X!')
    else:
        print(f'Точка с координатами {coordinate}, находится в {what_quarter(coordinate)} плоскости.')
except:
    print('Введите число!')