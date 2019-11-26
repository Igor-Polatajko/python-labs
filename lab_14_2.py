#!/usr/bin/env python
import sqlite3


class Item:
    def __init__(self, item_id, name, surname, phone_number, ):
        self.id = item_id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __repr__(self):
        return f"#{self.id} {self.name} {self.surname} {self.phone_number}"

    @staticmethod
    def db_store(method):
        def wrapper(*args, **kwargs):
            method(*args, **kwargs)
            DbConnector().db.commit()

        return wrapper

    @staticmethod
    def db_read(method):
        def wrapper(*args, **kwargs):
            results = method(*args, **kwargs).fetchall()
            return [Item(result[0], result[1], result[2], result[3]) for result in results]

        return wrapper


class Singleton(object):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class DbConnector(Singleton):
    def __init__(self):
        self.db = sqlite3.connect("items")
        self.db.cursor().execute(
            'CREATE TABLE IF NOT EXISTS items ('
            'id integer PRIMARY KEY,'
            'name text NOT NULL,'
            'surname text NOT NULL,'
            'phone_number text NOT NULL)')
        self.db.commit()


class ItemDao:
    @Item.db_store
    def __init__(self):
        self.db = DbConnector().db

    @Item.db_read
    def find_by_field(self, field_name, field_value):
        return self.db.cursor().execute(f"SELECT * FROM items WHERE {field_name} = ?", (field_value,))

    @Item.db_read
    def find_all(self):
        return self.db.cursor().execute("SELECT * FROM items")

    @Item.db_store
    def create(self, item):
        self.db.cursor().execute("INSERT INTO items (name, surname, phone_number)"
                                 " VALUES (?, ?, ?)", (item.name, item.surname, item.phone_number))
        self.db.commit()

    @Item.db_store
    def update(self, item):
        self.db.cursor().execute("UPDATE items SET name = ?, surname = ?, phone_number = ?"
                                 "WHERE id = ?", (item.name, item.surname, item.phone_number, item.id))

    @Item.db_store
    def delete(self, item_id):
        self.db.cursor().execute("DELETE FROM items WHERE id = ?", (item_id,))


class View:
    def show_footer(self):
        print("\n### Enter [menu] - to see the menu ###")
        return input("> ")

    def show_menu(self):
        print(
            "\n###### Menu #####\n"
            "Enter [list] - to show full list\n"
            "Enter [find id {item_id}] - to find by id\n"
            "Enter [find name {name}] - to find by name\n"
            "Enter [find phone {surname}] - to find by phone number\n"
            "Enter [rm {item_id}] - to remove the item\n"
            "Enter [add] - to add the item\n"
            "Enter [exit] - to exit\n"
        )
        return self.show_footer()

    def show_add_item_menu(self):
        print("\n##### Add item ######")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        phone_number = input("Enter phone number: ")
        return Item(None, name, surname, phone_number)

    def show_incorrect_input_error(self):
        print("\nIncorrect input")
        return self.show_footer()

    def show_items_list(self, items):
        print("\n #### Items ####")
        if isinstance(items, list):
            for item in items:
                print(item)
        else:
            print(items)
        return self.show_footer()


class ViewInputHandler:
    def __init__(self, view, item_dao):
        self.view = view
        self.item_dao = item_dao

    def handle_input(self, user_input="default"):
        user_input_parts = user_input.split()
        if len(user_input_parts) < 1:
            return self.view.show_incorrect_input_error()

        p0 = user_input_parts[0]
        if p0 == "list":
            return self.view.show_items_list(self.item_dao.find_all())
        if p0 == "find":
            if len(user_input_parts) != 3:
                return self.view.show_incorrect_input_error()
            selector = user_input_parts[1]
            param = user_input_parts[2]
            if selector == "id":
                return self.view.show_items_list(self.item_dao.find_by_field("id", param))
            if selector == "name":
                return self.view.show_items_list(self.item_dao.find_by_field("name", param))
            if selector == "phone":
                return self.view.show_items_list(self.item_dao.find_by_field("phone_number", param))
        if p0 == "rm":
            if len(user_input_parts) != 2:
                return self.view.show_incorrect_input_error()
            self.item_dao.delete(user_input_parts[1])
            return self.view.show_items_list(self.item_dao.find_all())
        if p0 == "add":
            item = self.view.show_add_item_menu()
            self.item_dao.create(item)
            return self.view.show_items_list(self.item_dao.find_all())
        if p0 == "exit":
            exit(0)
        if p0 == "menu":
            return self.view.show_menu()
        if p0 == "default":
            return self.view.show_footer()
        return self.view.show_incorrect_input_error()


class Controller:
    def run_app(self):
        view = View()
        item_dao = ItemDao()

        view_input_handler = ViewInputHandler(view, item_dao)

        previous_input = view_input_handler.handle_input()
        while True:
            previous_input = view_input_handler.handle_input(previous_input)


def main():
    controller = Controller()
    controller.run_app()


if __name__ == '__main__':
    main()
