#!/usr/bin/env python
import socket
import time
from datetime import datetime
from random import randint


class Server:
    def __init__(self, server):
        self.server = server

    def serve(self):
        self.server.listen(5)
        print('Start listening')

        while True:
            client, client_address = self.server.accept()
            print(f"Connection from {client_address}")
            self.__start_conversation_loop(client)
            client.close()
            print(f"Connection with {client_address} was closed")

    def __start_conversation_loop(self, client):
        self.__send_message(client, "Hello, what is your name??")
        username = self.__receive_message(client)
        self.__send_message(client, f"Nice to meet you, {username}. I am simple chatbot.\n"
                                    f"I will answer to your questions.\n"
                                    f"You may see the list of questions that I understand by typing "
                                    f"command: help.")
        while True:
            try:
                message = self.__receive_message(client).lower()
            except ConnectionResetError:
                print("Connection reset")
                break
            print(f"Received message: {message}")
            if message == "bye":
                self.__send_message(client, "Bye!!!")
                break

            self.__send_message(client, self.__generate_answer(message, username))
            time.sleep(0.1)

    def __generate_answer(self, message, username):
        if message == "help":
            return f"I understand the following commands:\n" \
                   f"bye   - stop our conversation\n" \
                   f"name  - I will try to mention your name\n" \
                   f"day   - I will say you what the day is today\n" \
                   f"hour  - I will send you current hour\n" \
                   f"random - I will generate random number for you\n"
        if message == "name":
            return f"Your name is {username}"
        if message == "day":
            return f"Today is {datetime.today().strftime('%A')}"
        if message == "hour":
            return f"Hour -  {datetime.now().hour}"
        if message == "random":
            return f"Random number for you - {randint(0, 100)}"

        return f"Ask me something else..."

    def __send_message(self, client, message):
        client.send(message.encode('utf-8'))

    def __receive_message(self, client):
        return client.recv(1024).decode('utf-8')


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9001
    server_socket.bind((host, port))
    server = Server(server_socket)
    server.serve()


if __name__ == '__main__':
    main()
