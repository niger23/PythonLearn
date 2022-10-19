# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def negafib (n):
#     result = [0, 1]
#     resultn = [0, 1]
#     for i in range(2,n+1):
#         next = result[i-1] + result[i-2]
#         if i%2 == 0:
#             resultn.append(-next)
#         else:
#             resultn.append(next)
#         result.append(next)
#     print(result)
#     print(resultn)
#     print(resultn[1:][::-1] + result)


# num = int(input("Введите число: "))
# fib = negafib(num)

def fibanachi(n):
    if n in (1, 2):
        return 1
    else:
        return fibanachi(n-1) + fibanachi(n-2)

N = int(input('Enter n: '))
fib_arr = []
for i in range(1, N + 1):
    fib_arr.append(fibanachi(i))
fib_arr.insert(0, 0)
for i in range(1, N + 1):
    fib_arr.insert(0, ((-1)**(i + 1)) * fibanachi(i))
print(fib_arr)
