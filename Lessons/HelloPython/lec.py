# print("Hello world")
# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = "hello world"
# a = 123
# b = 1.23

# print(s) # вывод строки
# print(a,'-',b,'-',s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = ['1','2','3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# print ('Введите a')
# a = float(input())
# print ('Введите b')
# b = float(input())
# print(a,' + ',b,' = ', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# Арифметические и сокращённые операции

# Логические операции

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# if, if-else

# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это же МАША!")
# elif username == "Марина":
#     print("Я так вас ждала, Марина!")
# elif username == "Ильнар":
#     print("Ильнар - топ)")
# else:
#     print("Привет, ", username)

# while

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print("Пожалуй")
#     print("хватит )")
# print(inverted)

# for

# for i in 'qwe - rty':
#     print(i)

# text = 'съешь ещё этих мягких французских булок'

# help(int)


# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #

# for c in text:
#     print(c)
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# def f(x):
#     if x == 1:
#         return "Целое"
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))