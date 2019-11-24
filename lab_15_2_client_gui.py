#!/usr/bin/env python
import socket
from tkinter import Tk, Listbox, Scrollbar, END, Text, Button, W, Toplevel, Label, Entry

from socketClient import Client

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9001


class ClientUI:
    def __init__(self, master, client):
        self.master = master
        self.client = client

        master.title("Chatroom")
        master.geometry("560x350")

        self.messages_list = Listbox(self.master, height=12, width=75, border=1)
        self.messages_list.grid(row=1, column=0, pady=20)
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=1, column=1, sticky=W)

        self.messages_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.messages_list.yview)

        self.message_input = Text(self.master, height=4, width=50)
        self.message_input.grid(row=2, column=0, rowspan=4, padx=50)

        self.send_button = Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, pady=20)

        master.bind('<Return>', self.return_press)

        self.username = PopupWindow(master, self.set_username, client)

    def set_username(self, username):
        self.username = username

    def return_press(self, event):
        self.send_message()

    def send_message(self):
        if not self.username:
            print("Username should be provided")
            exit(-1)
        message = self.message_input.get("1.0", END).rstrip()
        self.messages_list.insert(END, f"{self.username} > message")
        self.messages_list.yview(END)
        self.message_input.delete('1.0', END)
        self.client.send_message(message)


class PopupWindow(object):
    def __init__(self, master, callback, client):
        self.callback = callback
        self.client = client
        self.top = Toplevel(master)
        self.top.geometry("280x150")
        self.label = Label(self.top, text="Enter your username:", font=("Helvetica", 16))
        self.label.grid(row=0, column=0)
        self.entry = Entry(self.top, font=("Helvetica", 16))
        self.entry.grid(row=1, column=0, padx=20, pady=15)
        self.button = Button(self.top, text='Ok', command=self.submit)
        self.button.grid(row=2, column=0)

    def submit(self):
        username = self.entry.get().strip()
        self.callback(username)
        self.client.send_message(username)
        self.top.destroy()


def main():
    root = Tk()
    connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection_socket.connect((SERVER_HOST, SERVER_PORT))
        connection_socket.setblocking(False)
    except ConnectionRefusedError:
        print("Not able to connect!")
        exit(-1)
    client = Client(connection_socket)
    client_ui = ClientUI(root, client)
    root.mainloop()


if __name__ == "__main__":
    main()
