"""
Café and Wi-Fi website
Allow you to add, view, update and delete cafés
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "2432sgiooifsjhihdfusip9499"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafe_with_wifi.db"
Bootstrap(app)
db = SQLAlchemy(app)


# ------------------------------------
# database
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(400), nullable=False)
    img_url = db.Column(db.String(400), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(100), nullable=False)
    coffee_price = db.Column(db.String(100), nullable=False)

# # create database
# with app.app_context():
#     db.create_all()
# --------------------------------------


@app.route("/")
def home():
    """
    Show all Cafes
    :return:
    """
    with app.app_context():
        all_cafes = db.session.query(Cafe).all()

    return render_template("index.html", cafes=all_cafes)


@app.route("/cafe/<int:cafe_id>")
def get_cafe(cafe_id):
    """
    Get a cafe detail into of particular cafe with id
    :param cafe_id:
    :return:
    """
    with app.app_context():
        cafe = Cafe.query.get(cafe_id)
    return render_template("cafe_detail.html", cafe=cafe)


if __name__ == "__main__":
    app.run(debug=True)
