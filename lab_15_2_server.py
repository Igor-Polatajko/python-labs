#!/usr/bin/env python
import select
import socket


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
                    if sock == self.socket or ():
                        client, client_address = self.socket.accept()
                        print(f"Connection from {client_address}")
                        username = self.receive_message(client)
                        self.send_message(client, f"Hello there, {username}")
                        self.socket_list.append(client)
                        self.client_sockets[client] = username
                    else:
                        message = self.receive_message(sock)
                        if message:
                            print(f"Message: {message} from {self.client_sockets[sock]}")
                        else:
                            print(f"Closed connection from {sock['data']}")
                            self.socket_list.remove(sock)
                            del self.client_sockets[sock]

    def send_message(self, client, message):
        try:
            client.send(str(len(message)).encode('utf-8'))
            client.send(message.encode('utf-8'))
        except ConnectionResetError:
            return False

    def receive_message(self, client):
        try:
            message_len = int(client.recv(10).decode('utf-8'))
            return client.recv(message_len).decode('utf-8')
        except ConnectionResetError:
            return False


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 9001
    server_socket.bind((host, port))
    server = Server(server_socket)
    server.serve()


if __name__ == '__main__':
    main()
