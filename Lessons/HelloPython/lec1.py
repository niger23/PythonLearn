# Файлы
#  colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# with open('file.txt', 'a') as data:
#  data.write('line 11\n')
#  data.write('line 22\n')

# exit()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lec as h

# print(h.f(1))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a','s','d','f'))
# print(concatenatio('a','1'))
# print(concatenatio(1,2,3,4))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))

# print(list)

# КОРТЕЖИ

# a = (3,1,41,4) # a = (3,)
# print(a)
# print(a[-2])
# for item in a:
#     print(item)

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }

# print(dictionary['up']) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# dictionary['up'] = 'up'
# print(dictionary['up']) # ←

# for v in dictionary:
#     print(dictionary[v])

# МНОЖЕСТВА

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a)

# list1 = [1,2,3,4,5]

# print(list1.append(11))
# print(list1)


import json

BD=[12345,True,"яблоко", {"Миша": [898981646,464654654] }]


def load(): # загрузить из json
    fname='BD.json' #открываем файл
    with open(fname, 'r', encoding='utf-8') as fh: # открываем файл на чтение
        BD_local = json.load(fh) # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local

def save(): # сохранить в json
    with open('BD.json', 'w', encoding='utf-8') as fh: # открываем файл на запись
        fh.write(json.dumps(BD, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
    print('БД успещно сохранена')

#save()


BDnew = load ()
print(BDnew)