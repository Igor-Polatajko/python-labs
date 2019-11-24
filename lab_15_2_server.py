#!/usr/bin/env python
import socket

from socketServer import Server

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9001


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server = Server(server_socket)
    server.serve()


if __name__ == '__main__':
    main()
