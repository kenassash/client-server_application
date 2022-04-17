"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
что перед нами файл в неизвестной кодировке. Задача: открыть этот файл
БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""
from chardet import detect

LS = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for line in LS:
        file.write(f'{line}\n')
file.close()

with open('test_file.txt', 'rb') as file:
    CONTENT = file.read()
ENCODING = detect(CONTENT)['encoding']
print(ENCODING)

with open('test_file.txt', 'r', encoding=ENCODING) as file:
    CONTENT = file.read()
print(CONTENT)