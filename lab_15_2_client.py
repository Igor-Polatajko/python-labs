#!/usr/bin/env python
import socket
from time import sleep

from socketClient import Client

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9001


def main():
    connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection_socket.connect((SERVER_HOST, SERVER_PORT))
        connection_socket.setblocking(False)
    except ConnectionRefusedError:
        print("Not able to connect!")
        exit(-1)
    client = Client(connection_socket)
    username = input("Enter your username: ")
    client.send_message(username)
    while True:
        try:
            sleep(0.1)
            for message in client.receive_all():
                print(f"{message['user']}: {message['data']}")
            my_message = input(f"{username} > ")
            if my_message:
                client.send_message(my_message)
        except ConnectionAbortedError or ConnectionResetError:
            break
    connection_socket.close()


if __name__ == '__main__':
    main()
