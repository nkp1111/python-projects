"""
Ecommerce website
It shows products and accept payment on purchase.
"""
from flask import Flask, render_template, redirect, url_for, flash
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
        with app.app_context():
            all_user = db.session.query(User).all()
            # check if email aleardy exists
            for user in all_user:
                if user.email == form.email.data:
                    flash("Email already in use")
                    return redirect(url_for("register"))

            # if email is not register
            new_user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
            )
            db.session.add(new_user)
            db.session.commit()
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
                flash("need to register")
                return redirect(url_for("register"))
            elif user.password != form.password.data:
                flash("check password")
                return redirect(url_for("login"))
            else:
                flash("login")
                return redirect(url_for("home"))

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



