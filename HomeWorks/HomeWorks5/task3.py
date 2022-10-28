# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def delete_str(text, del_text):
    new_list = text.split(' ')
    for i in range(len(new_list)):
        if del_text in new_list[i]:
            new_list[i] = ''
    new_list = list(filter(None, new_list))

    return new_list


text = input('Введите текст: ')
del_text = input('Введите текст удаления: ')
new_list = delete_str(text, del_text)
print(new_list)