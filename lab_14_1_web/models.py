from sqlalchemy import Column, Integer, String

from lab_14_1_web.app_config import db


class ToDoItem(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=False, nullable=False)
    content = Column(String, unique=False, nullable=False)
    priority = Column(String, unique=False, nullable=False)
    completed = Column(String, unique=False, nullable=False)
