#!/usr/bin/env python
import os

from flask import Flask, render_template, redirect, request, abort
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


def _check_priority_validity(priority):
    return priority in ('HIGH', 'NORMAL', 'LOW')


@app.route('/')
def index():
    field = request.args.get("field")
    value = request.args.get("value")
    if field is not None and value is not None:
        search_enabled = True
        if hasattr(ToDoItem, field):
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
            if not _check_priority_validity(req_form['priority']):
                abort(400)
            item_to_store = ToDoItem(title=req_form['title'], content=req_form['content'],
                                     priority=req_form['priority'], completed='NO')
            db.session.add(item_to_store)
            db.session.commit()
            return redirect('/')
        else:
            error = "Fill all the fields!"
    return render_template('add.html', form=form, error=error)


@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit(item_id):
    form = AddEditForm()
    error = {}
    item = ToDoItem.query.filter_by(id=item_id).first()
    if not item:
        error = {'fatal': True, 'message': f'Item with id {item_id} not found'}
    elif request.method == 'POST':
        if form.validate_on_submit():
            req_form = request.form
            if not _check_priority_validity(req_form['priority']):
                abort(400)
            item.title = req_form['title']
            item.content = req_form['content']
            item.priority = req_form['priority']
            db.session.commit()
            return redirect('/')

        else:
            error = {'fatal': False, 'message': 'Fill all the fields!'}
    return render_template('edit.html', item=item, form=form, error=error)


@app.route('/delete/<item_id>', methods=['POST'])
def delete(item_id):
    ToDoItem.query.filter(ToDoItem.id == item_id).delete()
    db.session.commit()
    return redirect('/')


@app.route('/state/<item_id>/<action>', methods=['POST'])
def status_change(item_id, action):
    item = ToDoItem.query.filter_by(id=item_id).first()
    if item:
        if action == 'complete':
            item.completed = 'YES'
        elif action == 'uncomplete':
            item.completed = 'NO'
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run()
