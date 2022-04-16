"""
4. Преобразовать слова «разработка», «администрирование»,
«protocol», «standard» из строкового представления в байтовое и
выполнить обратное преобразование (используя методы encode и decode).
"""

def my_encode(ls):
    result = []
    for el in ls:
        result.append(el.encode('utf-8'))
    return result

def my_decode(ls):
    result = []
    for el in ls:
        result.append(el.decode('utf-8'))
    return result

LS = ['paзpaбoткa', 'aдминиcтpиpoвaниe', 'protocol', 'standard']

LS_B = my_encode(LS)
print(LS_B)
print(my_decode(LS_B))