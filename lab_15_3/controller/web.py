from flask import render_template

from lab_15_3.core.FlaskBaseController import route


class WebController:
    @route('/')
    def hello(self):
        return render_template("index.html")
