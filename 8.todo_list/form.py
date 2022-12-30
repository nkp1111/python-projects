from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class AddTaskForm(FlaskForm):
    task = StringField(label="",
                       validators=[DataRequired(), Length(1, 1000)],
                       render_kw={"placeholder": "Type your task here..."})
    # submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    email = StringField(label="Email: ", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class RegisterForm(FlaskForm):
    name = StringField(label="Name: ", validators=[DataRequired(), Length(1, 100)])
    email = StringField(label="Email: ", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
