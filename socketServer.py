import select

SERVER_NAME = 'Server'
HEADER_LENGTH = 10


class Server:
    def __init__(self, server_socket):
        self.socket = server_socket
        self.socket_list = [server_socket]
        self.client_sockets = dict()

    def serve(self):
        print("Start listening")
        self.socket.listen()

        while True:
            read_sockets = select.select(self.socket_list, [], [])

            for _sock in read_sockets:
                for ready_socket in _sock:
                    if ready_socket == self.socket:
                        self._handle_new_connection()
                    else:
                        self._handle_message(ready_socket)

    def _handle_new_connection(self):
        client, client_address = self.socket.accept()
        print(f"Connection from {client_address}")
        username = self.receive_message(client)
        self.send_message(client, SERVER_NAME, f"Hello there, {username}")
        self.send_to_all(client, f"{username} joined the group!")
        self.socket_list.append(client)
        self.client_sockets[client] = username

    def _handle_message(self, ready_socket):
        message = self.receive_message(ready_socket)
        if message:
            print(f"Message: {message} from {self.client_sockets[ready_socket]}")
            self.send_to_all(ready_socket, message)
        else:
            print(f"Closed connection from {ready_socket}")
            self.socket_list.remove(ready_socket)
            del self.client_sockets[ready_socket]

    def send_to_all(self, sending_client, message):
        for client_socket in self.client_sockets.keys():
            if client_socket != sending_client:
                if sending_client in self.client_sockets.keys():
                    from_user = self.client_sockets[sending_client]
                else:
                    from_user = SERVER_NAME
                self.send_message(client_socket, from_user, message)

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
        except Exception:
            return False
