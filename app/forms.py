from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BucketForm(FlaskForm):
    body = StringField('Enter your bucket name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TaskForm(FlaskForm):
    body = StringField('Enter your task name', validators=[DataRequired()])
    submit = SubmitField('Submit')