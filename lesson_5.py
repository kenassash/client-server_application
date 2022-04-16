"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

from subprocess import Popen, PIPE
from chardet import detect

def ping(URL):
    ARGS = ['ping', URL]
    PING = Popen(ARGS, stdout=PIPE)
    for line in PING.stdout:
        result = detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        line = line.decode('utf-8')
        print(result, line)

ping('ya.ru')
ping('youtube.com')