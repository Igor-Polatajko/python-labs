import errno

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

    def receive_all(self):
        messages = []
        try:
            while True:
                messages.append(self.receive_message())
        except IOError as e:
            if e.errno == errno.EAGAIN or e.errno == errno.EWOULDBLOCK:
                return messages
            print("IO error")
            exit(-1)
        except Exception:
            print("Error")
            exit(-1)
