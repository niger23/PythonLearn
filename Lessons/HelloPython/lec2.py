# list = []

# for i in range(1,101):
#     # if (i%2 == 0):
#     list.append(i)

# print(list)
# def f(x):
#     return x**3


# list = [(i,f(i)) for i in range(1,21) if i%2 == 0]
# print(list)

# path = 'Lessons/HelloPython/file3.txt'
# data = open(path, 'r')
# for line in data:
#     new = [int(x) for x in line.split(' ')]

# list = [(i, i**2) for i in new if i%2 == 0]
# print(list)

# li = [x for x in range(1,20)]

# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int,'1 2 3 4 555 6'.split()))

# for e in data:
#     print(e)
# print('-------')
# for e in data:
#     print(e)

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)


# path = 'Lessons/HelloPython/file3.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e,e **2))
# print(out)


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2),res))
# print(res)

users = ['user1','user2','user3','user4','user5']
ids = [4,5,9,14,7]
salary = [111,222,333]

data = list(enumerate(ids))
print(data)