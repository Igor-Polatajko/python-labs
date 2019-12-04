#!/usr/bin/env python
import sqlite3

ITEM_PRIORITY = {'1': 'HIGH (1)', '2': 'NORMAL (2)', '3': 'LOW (3)'}


class ToDoItem:
    def __init__(self, item_id, title, content, priority, completed):
        self.item_id = item_id
        self.title = title
        self.content = content
        self.priority = priority
        self.completed = completed

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
            return [ToDoItem(result[0], result[1], result[2], result[3], result[4]) for result in results]

        return wrapper


class DbConnector:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, 'db'):
            return
        self.db = sqlite3.connect("todo_items")
        self.db.cursor().execute(
            'CREATE TABLE IF NOT EXISTS todo_items ('
            'id integer PRIMARY KEY,'
            'title text NOT NULL,'
            'content text NOT NULL,'
            'priority text NOT NULL,'
            'completed integer NOT NULL)')
        self.db.commit()


class ToDoItemDao:
    @ToDoItem.db_store
    def __init__(self):
        self.db = DbConnector().db

    @ToDoItem.db_read
    def find_by_field(self, field_name, field_value):
        return self.db.cursor().execute(f"SELECT * FROM todo_items WHERE {field_name} LIKE ?", (f'%{field_value}%',))

    @ToDoItem.db_read
    def find_all(self):
        return self.db.cursor().execute("SELECT * FROM todo_items")

    @ToDoItem.db_store
    def create(self, item):
        self.db.cursor().execute("INSERT INTO todo_items (title, content, priority, completed)"
                                 " VALUES (?, ?, ?, ?)", (item.title, item.content, item.priority, item.completed))

    @ToDoItem.db_store
    def update(self, item):
        self.db.cursor().execute("UPDATE todo_items SET title = ?, content = ?, priority = ?, "
                                 "completed = ? WHERE id = ?",
                                 (item.title, item.content, item.priority,
                                  item.completed, item.item_id))

    @ToDoItem.db_store
    def delete(self, item_id):
        self.db.cursor().execute("DELETE FROM todo_items WHERE id = ?", (item_id,))


class View:
    def show_hint(self):
        print('\n###############################################\n'
              'type [help] - to see all the commands available\n'
              'type [exit] - to exit\n'
              '###############################################\n')

    def show_help(self):
        print('\n################ Commands ####################\n'
              'list - list all the items\n'
              'add - add new todo\n'
              'rm item_id - remove todo\n'
              'find field value - find by field value\n'
              'update item_id - find by field value\n'
              'complete item_id - mark as finished\n'
              'uncomplete item_id - unmark finished\n'
              'help - see all the commands available\n'
              'exit - exit the program\n'
              '###############################################\n')

    def item_view(self, item=None):
        old_title = ''
        old_content = ''
        old_priority = ''
        completed = 'No'
        if item:
            old_title = f' ({item.title})'
            old_content = f' ({item.content})'
            old_priority = f' ({item.priority})'
            completed = item.completed

        view_type = "Update" if item else "Add"
        print(f"### {view_type} item: ###")
        title = input(f"Enter title{old_title}: ")
        content = input(f"Enter content{old_content}: ")

        while True:
            priority = input(f"Enter priority{old_priority}: ")
            if priority in ('1', '2', '3'):
                break
            print("Error! Valid priority values: 1, 2, 3")

        return ToDoItem(None, title, content, ITEM_PRIORITY[priority], completed)

    def show_list(self, data):
        if len(data) < 1:
            print("Collection is empty!")
            return

        headers = {d: self._get_max_length(data, d, len(d)) for d in data[0].__dict__.keys()}

        print('##### List #####')
        for header in headers.keys():
            print(f"{header.capitalize():<{headers[header]}} | ", end='')
        print()
        for d in data:
            for header in headers.keys():
                d_dict = d.__dict__
                if header in d_dict.keys():
                    col = d_dict[header]
                else:
                    col = ''
                print(f"{col:<{headers[header]}} | ", end='')
            print()
        print()

    def _get_max_length(self, items, field, header_length):
        items_dicts = [item.__dict__ for item in items]
        length_list = [len(str(item[field])) for item in items_dicts if field in item.keys()]
        length_list.append(header_length)
        return max(length_list)


class ViewHandler:
    DB_COLUMNS_ADAPTER = {'item_id': 'id', 'title': 'title', 'content': 'content',
                          'priority': 'priority', 'completed': 'completed'}

    def __init__(self, view, todo_dao):
        self._view = view
        self._todo_dao = todo_dao

    def handle(self, user_input):
        i = user_input.strip().split()  # user_input_parts
        if len(i) == 0:
            return

        if i[0] == 'exit':
            exit(0)
        elif i[0] == 'help':
            self._view.show_help()
        elif i[0] == 'add':
            item = self._view.item_view()
            self._todo_dao.create(item)
        elif i[0] == 'list':
            self._view.show_list(self._todo_dao.find_all())
        elif i[0] == 'rm':
            if len(i) > 1:
                self._todo_dao.delete(i[1])
            else:
                print("Incorrect command syntax!")
                self._view.show_hint()
        elif i[0] == 'update':
            def _update(item):
                updated_item = self._view.item_view(item)
                updated_item.item_id = item.item_id
                self._todo_dao.update(updated_item)

            self.__update(i, _update)
        elif i[0] == 'complete':
            def _check(item):
                item.completed = 'YES'
                self._todo_dao.update(item)

            self.__update(i, _check)
        elif i[0] == 'uncomplete':
            def _uncheck(item):
                item.completed = 'NO'
                self._todo_dao.update(item)

            self.__update(i, _uncheck)
        elif i[0] == 'find':
            if len(i) > 2:
                field = i[1].lower()
                if field in self.DB_COLUMNS_ADAPTER.keys():
                    items = self._todo_dao.find_by_field(self.DB_COLUMNS_ADAPTER[field], i[2])
                    self._view.show_list(items)
                else:
                    print("Not valid field name")
                    print(f"Valid field names: {self.DB_COLUMNS_ADAPTER.keys()}")
            else:
                print("Incorrect command syntax!")
                self._view.show_hint()
        else:
            print("Unknown command!")
            self._view.show_hint()

    def __update(self, req, update_handler):
        if len(req) > 1:
            item = self._todo_dao.find_by_field('id', req[1])
            if item:
                item = item[0]
                update_handler(item)
            else:
                print('Item does not exist')
        else:
            print("Incorrect command syntax!")
            self._view.show_hint()


class Controller:
    def run(self):
        view = View()
        todo_dao = ToDoItemDao()
        view_handler = ViewHandler(view, todo_dao)

        view.show_hint()
        while True:
            user_input = input("> ")
            view_handler.handle(user_input)


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()
