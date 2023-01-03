"""
Ecommerce website
It shows products and accept payment on purchase.
"""
from flask import Flask, render_template
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
    form = RegisterForm()
    if form.validate_on_submit():
        pass

    return render_template("register.html", form=form, login=False)


if __name__ == "__main__":
    app.run(debug=True)



