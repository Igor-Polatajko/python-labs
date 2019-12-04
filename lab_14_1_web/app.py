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
    title = Column(String, unique=True, nullable=False)
    content = Column(String, unique=True, nullable=False)
    priority = Column(String, unique=True, nullable=False)
    completed = Column(String, unique=True, nullable=False)


@app.route('/')
def index():
    items = ToDoItem.query.all()
    return render_template('index.html', items=items)


@app.route('/item', methods=['GET', 'POST'])
def item():
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
    return render_template('add_edit.html', form=form, error=error)


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run()
