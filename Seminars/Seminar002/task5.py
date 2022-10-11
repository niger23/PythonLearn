# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def create_book (num):
    book = {}
    for i in range(1, num + 1):
        book[i] = i*3 +1
    return book

try:
    num = int(input("Введите число: "))
    print(create_book(num))
except:
    print('Введите число')