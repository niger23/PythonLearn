# задача 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def truth_check (digits):
    if not(digits[0] or digits[1] or digits[2]) == (not digits[0] and not digits[1] and not digits[2]):
        return True

try:
    print('Проверим тождественность утверждения: \n¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nдля всех значений')
    for i in range(2):
        for j in range(2):
            for k in range(2):
                digits = [i,j,k]
                if truth_check(digits) == True:
                    print(f'Для значений: {digits} тождественность: верна!')
                else:
                    print(f'Для значений: {digits} тождественность: неверна!')
        
except:
    print('Введите целое число')