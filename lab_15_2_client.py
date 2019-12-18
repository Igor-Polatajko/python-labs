#!/usr/bin/env python
from time import sleep

from socketClient import Client
from socketClientHelpers import Helpers, UserData

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9001


def main():
    socket_helpers = Helpers(SERVER_HOST, SERVER_PORT)
    try:
        connection_socket = socket_helpers.get_connection_socket()
    except ConnectionRefusedError:
        print("Not able to connect to the socket!")
        exit(-1)
    client = Client(connection_socket, socket_helpers.reconnect)
    user_data = UserData()
    user_data.set_username(input("Enter your username: "))
    client.send_message(user_data.get_user_name())
    while True:
        try:
            sleep(0.1)
            for message in client.receive_all():
                print(f"{message['user']}: {message['data']}")
            my_message = input(f"{user_data.get_user_name()} > ")
            if my_message:
                client.send_message(my_message)
        except ConnectionAbortedError or ConnectionResetError:
            print("Connection reset by server")
        except Exception:
            print("Error")
    connection_socket.close()


if __name__ == '__main__':
    main()
