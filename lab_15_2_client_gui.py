#!/usr/bin/env python
from tkinter import Tk, Listbox, Scrollbar, END


class ClientUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatroom")
        master.geometry("720x360")

        self.messages_list = Listbox(self.master, height=8, width=50, border=0)
        self.messages_list.grid(row=1, column=0, columnspan=5, rowspan=4, pady=20, padx=50)
        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.grid(row=1, column=5, rowspan=6)

        self.messages_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.messages_list.yview)

        for i in range(50):
            self.messages_list.insert(END, f"Message {i}")

        self.messages_list.yview(END)

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.grid(row=0, column=0)
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.grid(row=0, column=1)

    def greet(self):
        print("Greetings!")


def main():
    root = Tk()
    client_ui = ClientUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
