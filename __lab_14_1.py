#!/usr/bin/env python
import copy
import os


class ToDoItem:
    current_item_id = 1

    def __init__(self, title, content):
        self.item_id = ToDoItem.current_item_id
        self.completed = False
        self.title = title
        self.content = content
        ToDoItem.current_item_id += 1

    def __repr__(self):
        return f"{self.item_id}. {self.title} | {self.content} |" \
               f" {'DONE' if self.completed else ''}"


class ToDoItemDao:
    def __init__(self):
        self.__collection = []

    def create(self, item):
        self.__collection.append(item)

    def find_by_field(self, field_value, field='id'):
        def __comparator(item):
            item_field = getattr(item, field)
            if isinstance(item_field, str):
                return field_value in item_field
            else:
                return field_value == item_field

        return [item for item in self.__collection if __comparator(item)]

    def find_all(self):
        return copy.copy(self.__collection)

    def update(self, item):
        self.delete_ty_id(item.item_id)
        self.create(item)

    def delete_ty_id(self, item_id):
        self.__collection = list(filter(lambda it: it.item_id != item_id, self.__collection))


class View:
    @staticmethod
    def show_menu():
        print("""
####### Menu: #######
    Show all     - 1
    Search       - 2
    Add / Modify - 3
    Delete       - 4
    Exit         - 0
####################
        """)

    @staticmethod
    def search_by_menu():
        return

    @staticmethod
    def show_to_do_list(items, sort_by='item_id'):
        items.sort(key=lambda it: getattr(it, sort_by))
        print("\n###### Items: ######")
        for item in items:
            print(f"{item}")
        print("####################\n")

    @staticmethod
    def show_error_message_if_present(method_to_execute):
        def wrapper(*args):
            try:
                return method_to_execute(*args)
            except ValueError:
                View.show_message("Integer is expected")
            except:
                View.show_message("Some exception occurred")

        return wrapper

    @staticmethod
    def show_message(message):
        print(f"\n## {message} ##")


class Controller:
    def __init__(self, item_dao):
        self.item_dao = item_dao

    def run_app(self):
        self.__init_with_mock_data()

        while True:
            View.show_menu()
            executed_successfully = self.__handle_menu_choice(self.__get_user_input_integer("Your choice"))
            if not executed_successfully:
                View.show_message("Input was not handled successfully")
            os.system('pause')

    def __handle_menu_choice(self, user_choice):
        if user_choice == 0:
            View.show_message("Bye!!!")
            exit(0)
        if user_choice == 1:
            View.show_to_do_list(self.item_dao.find_all())
            return True
        if user_choice == 2:
            field_value = self.__get_user_input_string("Enter the field value: ")
            View.show_error_message_if_present(self.item_dao.find_by_field(field_value, 'title'))
            return True
        if user_choice == 3:
            return True
        if user_choice == 4:
            return True
        return False

    @View.show_error_message_if_present
    def __get_user_input_integer(self, message):
        return int(self.__get_user_input_string(f"{message}: "))

    def __get_user_input_string(self, message):
        return input(message)

    def __init_with_mock_data(self):
        for item in self.__get_mock_data():
            self.item_dao.create(item)

    def __get_mock_data(self):
        return [ToDoItem("item1", "do it"), ToDoItem("item2", "do it"), ToDoItem("item3", "description")]


def main():
    item_dao = ToDoItemDao()
    controller = Controller(item_dao)
    controller.run_app()


if __name__ == '__main__':
    main()
