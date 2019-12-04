from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddEditForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    priority = StringField('Priority', validators=[DataRequired()])
