"""
Café and Wi-Fi website
Allow you to add, view, update and delete cafés
"""
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from form import MyForm, PriceForm, DeleteForm

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


@app.route("/add_cafe", methods=["GET", "POST"])
def add_new_cafe():
    """
    Add new cafe on database
    :return:
    """
    form = MyForm()
    if form.validate_on_submit():
        with app.app_context():
            new_cafe = Cafe(
                name=form.name.data,
                map_url=form.map_url.data,
                img_url=form.img_url.data,
                location=form.location.data,
                seats=form.seats.data,
                has_toilet=form.has_toilet.data,
                has_wifi=form.has_wifi.data,
                has_sockets=form.has_sockets.data,
                can_take_calls=form.can_take_calls.data,
                coffee_price=form.coffee_price.data
            )
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("add_new_cafe.html", form=form)


@app.route("/update_price/<int:cafe_id>", methods=["GET", "POST"])
def update_price(cafe_id):
    """
    Edit coffee price info of a single cafe
    :param cafe_id:
    :return:
    """
    price_form = PriceForm()
    if price_form.validate_on_submit():
        with app.app_context():
            cafe_to_update = Cafe.query.get(cafe_id)
            cafe_to_update.coffee_price = price_form.price.data
            db.session.commit()
            return redirect(url_for("get_cafe", cafe_id=cafe_to_update.id))
    return render_template("edit_cafe.html", form=price_form)


@app.route("/delete_cafe/<int:cafe_id>", methods=["GET", "POST"])
def delete_cafe(cafe_id):
    """
    Delete cafe from the database.
    :param cafe_id:
    :return:
    """
    delete_form = DeleteForm()
    with app.app_context():
        cafe_to_delete = Cafe.query.get(cafe_id)
    if delete_form.validate_on_submit():
        if delete_form.confirm.data:
            with app.app_context():
                cafe_to_delete = Cafe.query.get(cafe_id)
                db.session.delete(cafe_to_delete)
                db.session.commit()

        return redirect(url_for("home"))

    return render_template("delete_cafe.html", cafe=cafe_to_delete, form=delete_form)


if __name__ == "__main__":
    app.run(debug=True)
