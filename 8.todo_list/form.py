from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length


class AddTaskForm(FlaskForm):
    task = StringField(label="",
                       validators=[DataRequired(), Length(1, 1000)],
                       render_kw={"placeholder": "Type your task here..."})
    # submit = SubmitField(label="Submit")

