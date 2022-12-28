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


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
