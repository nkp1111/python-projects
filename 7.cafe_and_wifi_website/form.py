from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, URL


class MyForm(FlaskForm):
    name = StringField(label="Name: ", validators=[DataRequired(), Length(1, 200)])
    map_url = StringField(label="Map URL: ", validators=[DataRequired(), URL()])
    img_url = StringField(label="Image URL: ", validators=[DataRequired(), URL()])
    location = StringField(label="Location: ", validators=[DataRequired(), Length(1, 300)])
    seats = StringField(label="Seats: ", validators=[DataRequired(), Length(1, 50)])
    has_toilet = BooleanField(label="Has toilet: ", default=True)
    has_wifi = BooleanField(label="Has Wifi: ", default=True, )
    has_sockets = BooleanField(label="Has Sockets: ", default=True)
    can_take_calls = BooleanField(label="Can take calls: ", default=True)
    coffee_price = StringField(label="Coffee price: ", validators=[DataRequired(), Length(1, 50)])
    submit = SubmitField(label="Submit")


class PriceForm(FlaskForm):
    price = StringField(label="New price: ", validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField(label="Submit")


class DeleteForm(FlaskForm):
    cancel = SubmitField(label="Cancel")
    confirm = SubmitField(label="Confirm")

