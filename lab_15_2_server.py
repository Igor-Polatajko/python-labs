#!/usr/bin/env python
import select
import socket

SERVER_NAME = 'Server'
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9001
HEADER_LENGTH = 10


class Server:
    def __init__(self, server_socket):
        self.socket = server_socket
        self.socket_list = [server_socket]
        self.client_sockets = dict()

    def serve(self):
        self.socket.listen()

        while True:
            read_sockets = select.select(self.socket_list, [], [])

            for _sock in read_sockets:
                for sock in _sock:
                    if sock == self.socket:
                        client, client_address = self.socket.accept()
                        print(f"Connection from {client_address}")
                        username = self.receive_message(client)
                        self.send_message(client, SERVER_NAME, f"Hello there, {username}")
                        self.send_to_all(client, f"{username} joined the group!")
                        self.socket_list.append(client)
                        self.client_sockets[client] = username
                    else:
                        message = self.receive_message(sock)
                        if message:
                            print(f"Message: {message} from {self.client_sockets[sock]}")
                            self.send_to_all(sock, message)
                        else:
                            print(f"Closed connection from {sock['raddr']}")
                            self.socket_list.remove(sock)
                            del self.client_sockets[sock]

    def send_to_all(self, client, message):
        for sock in self.client_sockets.keys():
            if sock != client:
                if client in self.client_sockets.keys():
                    from_user = self.client_sockets[client]
                else:
                    from_user = SERVER_NAME
                self.send_message(sock, from_user, message)

    def send_message(self, client, from_user, message):
        try:
            client.send(f"{len(from_user):<{HEADER_LENGTH}}".encode('utf-8')
                        + from_user.encode('utf-8')
                        + f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                        + message.encode('utf-8'))
        except ConnectionResetError:
            return False

    def receive_message(self, client):
        try:
            message_len = int(client.recv(HEADER_LENGTH).decode('utf-8'))
            return client.recv(message_len).decode('utf-8')
        except ConnectionResetError:
            return False


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server = Server(server_socket)
    server.serve()


if __name__ == '__main__':
    main()
