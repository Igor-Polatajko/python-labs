#!/usr/bin/env python
import os

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from lab_14_1_web.forms import AddEditForm

app = Flask(__name__, template_folder='views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy(app)


class ToDoItem(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=False, nullable=False)
    content = Column(String, unique=False, nullable=False)
    priority = Column(String, unique=False, nullable=False)
    completed = Column(String, unique=False, nullable=False)


@app.route('/')
def index():
    field = request.args.get("field")
    value = request.args.get("value")
    if field is not None and value is not None:
        search_enabled = True
        cls_field = getattr(ToDoItem, field)
        items = ToDoItem.query.filter(cls_field == value or cls_field.contains(value)).all()
    else:
        search_enabled = False
        items = ToDoItem.query.all()
    return render_template('index.html', items=items, search_enabled=search_enabled)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEditForm()
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            req_form = request.form
            item_to_store = ToDoItem(title=req_form['title'], content=req_form['content'],
                                     priority=req_form['priority'], completed='No')
            db.session.add(item_to_store)
            db.session.commit()
            return redirect('/')
        else:
            error = "Fill all the fields!"
    return render_template('add.html', form=form, error=error)


@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit(item_id):
    pass


@app.route('/items/<item_id>', methods=['DELETE'])
def delete(item_id):
    ToDoItem.query.filter(ToDoItem.id == item_id).delete()
    db.session.commit()
    return '', 204


@app.route('/items/<item_id>/<action>', methods=['POST'])
def status_change(item_id, action):
    return '', 200


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run()
