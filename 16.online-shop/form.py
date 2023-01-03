from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
    name = StringField(label="Name: ",
                       validators=[DataRequired(), Length(1, 200)],
                       render_kw={"placeholder": "Type your name here..."})
    email = StringField(label="Email: ",
                        validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Type your email here..."})
    password = PasswordField(label="Password: ",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Type your password here..."})
    submit = SubmitField(label="Submit")


class LoginForm(FlaskForm):
    email = StringField(label="Email: ",
                        validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Type your email here..."})
    password = PasswordField(label="Password: ",
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Type your password here..."},)
    submit = SubmitField(label="Submit")

