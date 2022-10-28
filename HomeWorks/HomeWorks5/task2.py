# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding (text):
    count = 1
    cod = ''
    for i in range(1, len(text)):
        if text[i-1] == text[i]:
            count+=1
            if i == len(text)-1:
                cod += str(count) + text[i]
        else:
            cod += str(count) + text[i-1]
            count = 1
    return cod

def encoding(text):
    encod = ''
    for i in range(len(text)):
        if text[i].isdigit():
            if text[i+1].isdigit():
                encod += (int(text[i:i+2])*text[i+2])
            else:
                encod += (int(text[i])*text[i+1])
    return encod


def save(text):
    with open('HomeWorks/HomeWorks5/task2_save.txt', 'w') as ff:
        ff.write(text)
    print('Файл task2_save.txt успешно сохранен')

def load ():
    with open('HomeWorks/HomeWorks5/task2_load.txt', 'r') as ff:
        text = ff.read()
    print('Файл task2_load.txt успешно загружен')
    return text

text = load()
print(f'Загружено: \n{text}')
cod = coding(text)
print(f'Закодировали этот код: \n{cod}')
save(cod)
encod = encoding(cod)
print(f'Раскодировали этот код: \n{encod}')
