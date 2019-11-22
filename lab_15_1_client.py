#!/usr/bin/env python
import socket


class Client:
    def __init__(self, connection_socket):
        self.__connection_socket = connection_socket

    def receive_message(self):
        return self.__connection_socket.recv(1024).decode('utf-8')

    def send_message(self, message):
        return self.__connection_socket.send(message.encode('utf-8'))


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
    while True:
        try:
            print(f"Server: {client.receive_message()}")
            client.send_message(input("You: "))
        except ConnectionAbortedError or ConnectionResetError:
            break
    connection_socket.close()


if __name__ == '__main__':
    main()
