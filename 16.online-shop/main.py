"""
Ecommerce website
It shows products and accept payment on purchase.
"""
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from form import RegisterForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "lsdgh88y8ywr94y5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(400), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    register user
    :return:
    """
    form = RegisterForm()
    if form.validate_on_submit():
        pass
        print("register")

    return render_template("register.html", form=form, login=False)


@app.route("/login")
def login():
    """
    allow login for registered user
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        pass
        print("login")
    return render_template("register.html", form=form, login=True)


@app.route("/logout")
def logout():
    """
    allow logout to logged-in user
    :return:
    """
    print("logout")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)



