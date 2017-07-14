from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from app.models import User, Database


class BucketForm(FlaskForm):
    body = StringField('Enter your bucket name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TaskForm(FlaskForm):
    body = StringField('Enter your task name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    # username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
    #                                       'Usernames must have only letters, '
    #                                       'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    # def validate_email(self, field):
    #     if db.find_user_by_email(email=field.data):
    #         raise ValidationError('Email already registered.')



class NewBucketForm(FlaskForm):
    name = StringField("What's the name of this bucket-list?", validators=[DataRequired()])
    description = TextAreaField("Can you describe this bucket?")
    submit = SubmitField('Submit')

class NewTaskForm(FlaskForm):
    description = TextAreaField("Enter new task", validators=[DataRequired()])
    submit = SubmitField('Submit')