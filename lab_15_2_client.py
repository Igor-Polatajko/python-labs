#!/usr/bin/env python
import socket

HEADER_LENGTH = 10


class Client:
    def __init__(self, connection_socket):
        self.__connection_socket = connection_socket

    def receive_message(self):
        user_len = int(self.__connection_socket.recv(HEADER_LENGTH).decode('utf-8'))
        user = self.__connection_socket.recv(user_len).decode('utf-8')
        message_len = int(self.__connection_socket.recv(HEADER_LENGTH).decode('utf-8'))
        message = self.__connection_socket.recv(message_len).decode('utf-8')
        return {'user': user, 'data': message}

    def send_message(self, message):
        self.__connection_socket.send(f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                                      + message.encode('utf-8'))


def main():
    connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9001
    try:
        connection_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Not able to connect!")
        exit(-1)
    client = Client(connection_socket)

    username = input("Enter your username: ")
    client.send_message(username)
    while True:
        try:
            message = client.receive_message()
            print(f"{message['user']}: {message['data']}")
        except ConnectionAbortedError or ConnectionResetError:
            break
    connection_socket.close()


if __name__ == '__main__':
    main()
