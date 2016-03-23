# -*- coding: utf-8 -*-
import socket
import os

socket = socket.socket()#создание сокета
socket.bind(('localhost', 8000))# связываем сокет с хостом и портом
#С помощью метода listen мы запустим для данного сокета режим прослушивания.
# максимальное количество подключений в очереди-1.
socket.listen(1)
if __name__ == "__main__":
    while True:
        #мы можем принять подключение с помощью метода accept,
        #который возвращает кортеж с двумя элементами: новый сокет и адрес клиента
        conn, addr  = socket.accept()
        #чтобы получить данные нужно воспользоваться методом recv,
        #который в качестве аргумента принимает количество байт для чтения -1024
        data =conn.recv(1024).decode()
        print(data)
        result = data.split('\n')[0].split(' ')[1]
        page = './' + result
        print(result)
        if not os.path.isfile(page):
                page = './index.html'

        filePage = open(page, 'r')
        answer = ("""HTTP/1.1 200 OK\n\n\n""" + filePage.read())
        conn.send(answer.encode())
        filePage.close()
    conn.close()#закрываем сединение
    socket.close()
