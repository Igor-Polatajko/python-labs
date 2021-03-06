import socket
from time import sleep


class UserData:
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(UserData)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_username'):
            return
        self._username = ''

    def set_username(self, username):
        self._username = username

    def get_user_name(self):
        return self._username


class Helpers:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def get_connection_socket(self):
        connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_socket.connect((self._host, self._port))
        connection_socket.setblocking(False)
        return connection_socket

    def reconnect(self):
        print("Reconnection timeout 5 sec")
        sleep(5)
        return self.get_connection_socket(), UserData().get_user_name()
