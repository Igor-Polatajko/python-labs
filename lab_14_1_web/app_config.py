import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy(app)
