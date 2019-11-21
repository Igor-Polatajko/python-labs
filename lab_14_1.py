#!/usr/bin/env python
import abc
import copy


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


class AbstractViewItem(abc.ABC):
    @abc.abstractmethod
    def handle_choice(self, user_choice):
        pass

    @abc.abstractmethod
    def show(self):
        pass


class MainMenuItem(AbstractViewItem):
    def show(self):
        print("""
####### Menu: #######
    Show all     - 1
    Search       - 2
    Add / Modify - 3
    Delete       - 4
    Exit         - 0
####################
""")

    def handle_choice(self, user_choice):
        pass


class ToDoList(AbstractViewItem):
    def show(self):
        print("""
####### Menu: #######
    Show all     - 1
    Search       - 2
    Add / Modify - 3
    Delete       - 4
    Exit         - 0
####################
""")

    def handle_choice(self, user_choice):
        pass


class Controller:
    def __init__(self, item_dao):
        self.item_dao = item_dao

    def run_app(self):
        self.__init_with_mock_data()

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
