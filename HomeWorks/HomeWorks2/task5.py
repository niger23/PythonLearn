# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
# Но теперь количество предикатов не три, а генерируется 
# случайным образом от 5 до 25, проверяем это утверждение 
# 100 раз, с помощью модуля time выводим на экран , сколько 
# времени отработала программа.

from random import randint
import time

def truth_check (num):
    for j in range(num):
        left = 0
        right = 1
        for i in range(randint(5,25)):
            new_item = randint(0,1)
            left = left or new_item
            right = right and not(new_item)
        left = not(left)
        print(f'{j+1} проверка тождественности! Результат: {left == right}')
print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
num = int(input('Введите сколько раз будем проверять: '))
start_time = time.perf_counter()
truth_check(num)
end_time = time.perf_counter()
print(f"Вычисление заняло {round(end_time - start_time, 5)} секунд")
