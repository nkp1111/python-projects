"""
Ecommerce website
It shows products and accept payment on purchase.
"""
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
import json

from form import RegisterForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "lsdgh88y8ywr94y5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
Bootstrap(app)
db = SQLAlchemy(app)

# flask login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# flask sqlalchemy
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(400), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()


# app routes
@app.route("/")
def home():
    user_name = ""
    if current_user.is_authenticated:
        user_name = current_user.name
    with open("product.json") as file:
        products = json.load(file)
    return render_template("index.html", user=user_name, products=products)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    register user
    :return:
    """
    form = RegisterForm()
    if form.validate_on_submit():
        with app.app_context():
            all_user = db.session.query(User).all()
            # check if email already exists
            for user in all_user:
                if user.email == form.email.data:
                    flash("Email already in use")
                    return redirect(url_for("register"))

            # if email is not registered
            hashed_password = generate_password_hash(
                password=form.password.data,
                method="pbkdf2:sha256",
                salt_length=12,
            )
            new_user = User(
                name=form.name.data,
                email=form.email.data,
                password=hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        return redirect(url_for("home"))

    return render_template("register.html", form=form, login=False)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    allow login for registered user
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        with app.app_context():
            user = User.query.filter_by(email=form.email.data).first()
            if not user:
                flash("need to register first")
                return redirect(url_for("register"))
            elif not check_password_hash(user.password, form.password.data):
                flash("check your password and try again")
                return redirect(url_for("login"))
            else:
                login_user(user)
                return redirect(url_for("home"))

    return render_template("register.html", form=form, login=True)


@login_required
@app.route("/logout")
def logout():
    """
    allow logout to logged-in user
    :return:
    """
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)



